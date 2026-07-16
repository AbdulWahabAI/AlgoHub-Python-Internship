import json
import os
from datetime import datetime

# --- Custom Exception Classes ---
# These handle specific diary errors so the app doesn't crash on bad inputs.

class DiaryError(Exception):
    """Base exception for all diary-related issues."""
    pass

class DiaryReadError(DiaryError):
    """Raised when we can't read the JSON file."""
    pass

class DiaryWriteError(DiaryError):
    """Raised when we can't save data to the JSON file."""
    pass

class EntryValidationError(DiaryError):
    """Raised when title or content inputs are empty or invalid."""
    pass

class EntryNotFoundError(DiaryError):
    """Raised when a user searches for an ID that doesn't exist."""
    pass


# --- JSON File Handler Class ---
# This class handles saving and loading the diary data.

class DiaryFileManager:
    def __init__(self, filepath="diary_storage.json"):
        self.filepath = filepath

    def load_raw_data(self):
        """Loads entries from the JSON file. Returns an empty list if no file exists yet."""
        if not os.path.exists(self.filepath):
            return []

        try:
            with open(self.filepath, 'r', encoding='utf-8') as file:
                content = file.read().strip()
                if not content:
                    return []
                return json.loads(content)
        except json.JSONDecodeError:
            raise DiaryReadError("The database file is corrupted or empty.")
        except PermissionError:
            raise DiaryReadError("Access denied. Cannot read the storage file.")
        except Exception as e:
            raise DiaryReadError(f"Error loading file: {str(e)}")

    def save_raw_data(self, data):
        """Saves the Python list of dicts directly into the JSON file."""
        try:
            with open(self.filepath, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
        except PermissionError:
            raise DiaryWriteError("Access denied. Cannot write to the storage file.")
        except Exception as e:
            raise DiaryWriteError(f"Error saving file: {str(e)}")


# --- Main Diary Logic ---
# Handles the core operations: adding, deleting, and searching entries.

class PersonalDiary:
    def __init__(self, file_manager):
        self.file_manager = file_manager
        self.entries = []
        self.reload_entries()

    def reload_entries(self):
        """Syncs the internal list with whatever is in the JSON file."""
        self.entries = self.file_manager.load_raw_data()

    def create_entry(self, title, content, tags=None):
        """Validates inputs, assigns a unique ID, and appends the entry."""
        clean_title = title.strip()
        clean_content = content.strip()

        # Validation checks
        if not clean_title:
            raise EntryValidationError("The diary title cannot be blank.")
        if not clean_content:
            raise EntryValidationError("The diary content body cannot be blank.")

        # Clean up tags (strip spaces and make lowercase)
        processed_tags = []
        if tags:
            for tag in tags:
                if tag.strip():
                    processed_tags.append(tag.strip().lower())

        # Generate sequential ID (adds 1 to the highest ID, or starts at 1)
        next_id = 1
        if self.entries:
            next_id = max(entry["id"] for entry in self.entries) + 1

        new_entry = {
            "id": next_id,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "title": clean_title,
            "content": clean_content,
            "tags": processed_tags
        }

        self.entries.append(new_entry)
        self.file_manager.save_raw_data(self.entries)
        return new_entry

    def get_all(self):
        """Returns all entries."""
        return self.entries

    def get_by_id(self, entry_id):
        """Finds a specific diary entry or raises an error if missing."""
        for entry in self.entries:
            if entry["id"] == entry_id:
                return entry
        raise EntryNotFoundError(f"No diary entry found with ID: {entry_id}")

    def search(self, keyword):
        """Searches titles, contents, or tags for matching text."""
        query = keyword.strip().lower()
        if not query:
            return self.entries

        results = []
        for entry in self.entries:
            in_title = query in entry["title"].lower()
            in_content = query in entry["content"].lower()
            in_tags = any(query in tag for tag in entry["tags"])
            
            if in_title or in_content or in_tags:
                results.append(entry)
        return results

    def delete_by_id(self, entry_id):
        """Deletes an entry and shifts remaining IDs to avoid gaps in sequence."""
        target = self.get_by_id(entry_id) # Verifies if it exists
        self.entries.remove(target)

        # Re-index remaining entries so IDs stay clean (1, 2, 3...)
        for index, entry in enumerate(self.entries):
            entry["id"] = index + 1

        self.file_manager.save_raw_data(self.entries)