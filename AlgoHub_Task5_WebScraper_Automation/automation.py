import os
import shutil
import time
import schedule

def organize_download_directory():
    source_dir = "./sample_downloads/"
    
    if not os.path.exists(source_dir):
        os.makedirs(source_dir)
        print(f"Created sample directory at: {source_dir}")
        # Create dummy files for demonstration
        open(os.path.join(source_dir, "report.pdf"), "w").close()
        open(os.path.join(source_dir, "image.png"), "w").close()
        open(os.path.join(source_dir, "data.csv"), "w").close()

    folders = {
        "Documents": [".pdf", ".docx", ".txt", ".csv"],
        "Images": [".jpg", ".jpeg", ".png", ".gif"]
    }

    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False
            
            for category, extensions in folders.items():
                if file_ext in extensions:
                    dest_folder = os.path.join(source_dir, category)
                    if not os.path.exists(dest_folder):
                        os.makedirs(dest_folder)
                    
                    shutil.move(file_path, os.path.join(dest_folder, filename))
                    print(f"Moved {filename} to {category}/")
                    moved = True
                    break
            
            if not moved:
                other_folder = os.path.join(source_dir, "Others")
                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)
                shutil.move(file_path, os.path.join(other_folder, filename))
                print(f"Moved {filename} to Others/")

def automated_job():
    print("[Automation Triggered] Running scheduled file organization task...")
    organize_download_directory()
    print("Task completed successfully.\n")

if __name__ == "__main__":
    print("Task Automation Scheduler Initialized...")
    
    # Schedule the job to run every 10 seconds (for testing) or daily
    schedule.every(10).seconds.do(automated_job)
    
    print("Waiting for scheduled triggers... Press Ctrl+C to exit.")
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Scheduler stopped by user.")