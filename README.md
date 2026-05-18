# Smart File Classifier 🚀

A lightweight, automated Python script designed to organize messy directories instantly. It scans a target folder and automatically categorizes audio, video, and picture files into their respective folders.

This tool was born out of a real-world necessity. Working in customer service, I handled dozens of media files sent by clients daily. Manually sorting them was a tedious, time-consuming task—so I built this automation tool to reduce a 10-minute daily chore into a 3-second click.

---

## ✨ Features

- **Dynamic Path Input**: Allows users to specify any folder path dynamically at runtime.
- **Data Standardization**: Automatically handles mixed-case file extensions (e.g., `.JPG`, `.Jpg`, and `.jpg` are all treated equally).
- **Safety First**: Uses `is_file()` checks to prevent moving existing directories or core system folders by mistake.
- **Smart Directory Creation**: Automatically generates target folders (`audio`, `video`, `picture`) if they don't already exist.
- **Real-time Metrics**: Displays a clean summary counting exactly how many files were successfully archived.

---

## 🛠️ Supported Formats

| Category | Supported Extensions |Target Folder |
| :--- | :--- | :--- |
| 🎵 **Audio** | `.mp3`, `.flac`, `.wav`, `.m4a` | `/audio` |
| 🎬 **Video** | `.mp4`, `.mkv`, `.avi`, `.mov` | `/video` |
| 🖼️ **Picture** | `.jpg`, `.jpeg`, `.png`, `.gif` | `/picture` |

---

## 🚀 How to Run

### Prerequisites
Make sure you have Python 3.x installed on your system.

### Steps
1. Clone or download this repository.
2. Open your terminal or command prompt.
3. Run the script using:
   ```bash
   python p.py
