# Personal Diary CLI (AlgoHub Week 3 Task)

This is a simple terminal diary program built with Python. It lets you write, view, search, and delete daily diary entries. Your logs are saved locally in a JSON file, and the program uses custom error handling so it won't crash if you make a typo or enter a wrong option.

---

## Deliverables & Verification

- Demo Video: [Click Here to Watch the Walkthrough](PASTE_YOUR_VIDEO_LINK_HERE)
- LinkedIn Post: [Click Here to View the Project Post](PASTE_YOUR_LINKEDIN_POST_LINK_HERE)

---

## Features

- Add Logs: Save a new diary entry with a title, body, and tags. The app automatically assigns an ID and the current date/time.
- View All: Displays a list of all your saved logs (ID, date, and title) in the terminal.
- Read Specific Entry: Type in an ID to read the full body and tags of that specific diary entry.
- Search: Search your entries by typing in a keyword or a tag.
- Delete and Re-index: Delete any entry by ID. The app will automatically shift the remaining IDs so there are no empty gaps in your numbering list.
- Error Handling: Safe inputs that won't crash the program if you leave fields blank or type letters instead of numbers.

---

## Tech Stack

- Python 3.10+
- Built-in modules: json, os, datetime, sys

---

## Project Structure

AlgoHub_Task3_PersonalDiary/
|
├── diary_manager.py
├── main.py
├── requirements.txt
└── README.md

---

## Local Database

- File Name: diary_storage.json
- Storage: Saved in the main folder automatically on your first entry.
- Format: Plain JSON using UTF-8 encoding.

---

## How to Set Up and Push to GitHub

If you are setting this up in your VS Code terminal, run these commands to link your local folder to your GitHub repository:

### 1. Initialize Git and Commit Files
```bash
git init
git add .
git commit -m "Initial commit of Week 3 Personal Diary project"