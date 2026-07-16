import sys
from diary_manager import DiaryFileManager, PersonalDiary
from diary_manager import DiaryError, EntryNotFoundError, EntryValidationError

def print_line():
    print("-" * 50)

def main():
    # Setup our file manager and diary system
    storage = DiaryFileManager("diary_storage.json")
    diary = PersonalDiary(storage)

    print("==================================================")
    print("             MY PERSONAL DIARY (CLI)              ")
    print("==================================================")

    while True:
        print("\nWhat would you like to do?")
        print("1) Add a new entry")
        print("2) View all entries")
        print("3) Read a specific entry")
        print("4) Search entries by keyword/tag")
        print("5) Delete an entry")
        print("6) Exit")
        print_line()

        choice = input("Select an option (1-6): ").strip()

        try:
            if choice == "1":
                print("\n--- New Entry ---")
                title = input("Enter Title: ")
                content = input("Write your thoughts: ")
                tags_input = input("Enter tags (comma separated, optional): ")
                
                # Turn comma-separated string into a clean list
                tags = []
                if tags_input.strip():
                    tags = [t.strip() for t in tags_input.split(",")]

                entry = diary.create_entry(title, content, tags)
                print(f"\n[Success] Entry #{entry['id']} saved successfully!")

            elif choice == "2":
                entries = diary.get_all()
                if not entries:
                    print("\nYour diary is empty. Try adding some entries first!")
                else:
                    print("\n--- All Diary Entries ---")
                    print(f"{'ID':<5} | {'Date & Time':<20} | {'Title'}")
                    print_line()
                    for entry in entries:
                        print(f"{entry['id']:<5} | {entry['timestamp']:<20} | {entry['title']}")

            elif choice == "3":
                entry_id = int(input("\nEnter the ID of the entry to view: "))
                entry = diary.get_by_id(entry_id)
                
                print_line()
                print(f"ENTRY #{entry['id']}: {entry['title'].upper()}")
                print(f"Date: {entry['timestamp']}")
                print(f"Tags: {', '.join(entry['tags']) if entry['tags'] else 'None'}")
                print_line()
                print(entry['content'])
                print_line()

            elif choice == "4":
                keyword = input("\nEnter tag or keyword to search: ")
                results = diary.search(keyword)
                
                if not results:
                    print(f"\nNo entries matched '{keyword}'.")
                else:
                    print(f"\nSearch Results ({len(results)} found):")
                    for entry in results:
                        print(f"ID: {entry['id']} | Date: {entry['timestamp']} | Title: {entry['title']}")

            elif choice == "5":
                entry_id = int(input("\nEnter the ID of the entry to delete: "))
                # Fast check to see if the ID actually exists before asking for confirmation
                diary.get_by_id(entry_id)
                
                confirm = input(f"Are you sure you want to delete entry #{entry_id}? (yes/no): ").lower().strip()
                if confirm == "yes":
                    diary.delete_by_id(entry_id)
                    print(f"\n[Success] Entry #{entry_id} has been deleted.")
                else:
                    print("\nDeletion cancelled.")

            elif choice == "6":
                print("\nSaving files and exiting. Bye!")
                break

            else:
                print("\n[Error] Invalid choice. Please pick a number from 1 to 6.")

        except ValueError:
            print("\n[Input Error] Please enter a valid number.")
        except EntryNotFoundError as e:
            print(f"\n[Not Found] {e}")
        except EntryValidationError as e:
            print(f"\n[Validation Error] {e}")
        except DiaryError as e:
            print(f"\n[System Error] {e}")
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Exiting safely...")
            break
        finally:
            pass # Keep here for good practice

if __name__ == "__main__":
    main()