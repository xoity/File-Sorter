import os
import shutil
import time

# Get the user's Downloads folder
downloads_folder = os.path.expanduser("~/Downloads")

# Set the allowed extensions
allowed_extensions = {".txt", ".png", ".jpg", ".py", ".pdf", ".docx", ".xlsx", ".pptx", ".jpeg"}

# Define recognized folder names
recognized_folders = {
    "text_files": ".txt",
    "images": {".png", ".jpg", ".gif", ".jpeg"},
    "python_files": ".py",
    "documents": {".pdf", ".docx", ".xlsx", ".pptx"},
}

# Ensure recognized destination folders exist
desktop_folder = os.path.join(os.path.expanduser("~"), "Desktop")
for folder in recognized_folders:
    folder_path = os.path.join(desktop_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Continuously loop to monitor and sort files
while True:
    files = os.listdir(downloads_folder)
    for file in files:
        file_path = os.path.join(downloads_folder, file)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file)[1].lower()
            if file_extension in allowed_extensions:
                # Determine the destination folder based on recognized extensions
                destination_folder = None
                for folder, extensions in recognized_folders.items():
                    if file_extension in extensions:
                        destination_folder = folder
                        break
                if destination_folder is None:
                    destination_folder = "other_files"
                
                destination_path = os.path.join(desktop_folder, destination_folder)
                try:
                    shutil.move(file_path, destination_path)
                    print(f"{file} moved to {destination_folder} folder.")
                except Exception as e:
                    print(f"Error moving {file}: {str(e)}")
    time.sleep(1)  # Wait for 1 second before checking again
