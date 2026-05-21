from pathlib import Path
import shutil
import hashlib       
import tkinter as tk 
from tkinter import filedialog, messagebox

# ==========================================
# 🧠 Core Algorithm: Calculate Unique File Hash (MD5)
# ==========================================
def calculate_file_hash(file_path):
    """
    Reads the file binary data and returns a unique MD5 hex string as a file fingerprint.
    """
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        while content := f.read(8192):
            hasher.update(content)
    return hasher.hexdigest()

# ==========================================
# 🎨 Logic & Event Handler: Triggered when user clicks 'Run Organizer'
# ==========================================
def run_classifier_action():
    # 1. Fetch the target folder path from the entry widget dynamically
    raw_path = path_entry.get()
    folder = Path(raw_path.strip())
    
    # 2. Path Validation: Intercept and error out if the directory doesn't exist
    if not raw_path or not folder.exists():
        messagebox.showerror("Error", "The folder path is invalid or does not exist!")
        return

    # 3. Initialize metrics counters for each category
    audio_count = 0
    video_count = 0
    picture_count = 0
    duplicate_count = 0  # Counter for redundant files

    # 4. Define target subdirectories (including duplicate shelter)
    audio_dir = folder / 'audio'
    video_dir = folder / 'video'
    picture_dir = folder / 'picture'
    duplicate_dir = folder / 'duplicates'  

    # Automatically create folders if they do not exist
    audio_dir.mkdir(exist_ok=True)
    video_dir.mkdir(exist_ok=True)
    picture_dir.mkdir(exist_ok=True)
    duplicate_dir.mkdir(exist_ok=True)    

    # 5. Mapping extensions for dynamic sorting
    audio_exts = ['.mp3', '.flac', '.wav', '.m4a']
    video_exts = ['.mp4', '.mkv', '.avi', '.mov']
    picture_exts = ['.jpg', '.jpeg', '.png', '.gif']

    # Initialize an empty set to act as our hash registry ledger
    seen_hashes = set()

    # 6. Main classification and deduplication loop
    for file in folder.iterdir():
        # Ensure only standalone files are processed, bypassing newly created directories
        if file.is_file():
            
            # 🛡️ 【Core Deduplication Layer】Intercept duplicates first
            file_hash = calculate_file_hash(file)
            
            if file_hash in seen_hashes:
                # Content identical hash match found; move directly to duplicate directory
                shutil.move(file, duplicate_dir)
                duplicate_count += 1
            else:
                # New unique file detected; register hash and standard classify by extension
                seen_hashes.add(file_hash)
                
                ext = file.suffix.lower()
                if ext in audio_exts:
                    shutil.move(file, audio_dir)
                    audio_count += 1
                elif ext in video_exts:
                    shutil.move(file, video_dir)
                    video_count += 1
                elif ext in picture_exts:
                    shutil.move(file, picture_dir)
                    picture_count += 1

    # 7. Deliver results back to user via modern messagebox dialog
    result_message = (
        f"✨ Processed! This batch of files has been archived:\n\n"
        f"🎵 Audio files: {audio_count}\n"
        f"🎬 Video files: {video_count}\n"
        f"🖼️ Image files: {picture_count}\n"
        f"👯 Duplicate files: {duplicate_count}" 
    )
    messagebox.showinfo("Success", result_message)


# ==========================================
# 📂 Browse Action: Let users interact via native file picker
# ==========================================
def select_folder_action():
    selected_dir = filedialog.askdirectory()
    if selected_dir:
        path_entry.delete(0, tk.END)  
        path_entry.insert(0, selected_dir)  


# ==========================================
# 🚀 Desktop Software GUI Layout Initialization
# ==========================================
root = tk.Tk()
root.title("Whitecat Smart Sorter v2.0")
root.geometry("450x220")

title_label = tk.Label(root, text="Select the directory you want to clean up:", pady=10)
title_label.pack()

path_entry = tk.Entry(root, width=50)
path_entry.pack(pady=5)

browse_btn = tk.Button(root, text="Browse Folder", command=select_folder_action)
browse_btn.pack(pady=5)

start_btn = tk.Button(root, text="🚀 Run Organizer", command=run_classifier_action, bg="green", fg="white", pady=5)
start_btn.pack(pady=15)

root.mainloop()