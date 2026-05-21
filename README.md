# Smart File Sorter v2.0 🚀

[🇨🇳 简体中文版](./README_zh.md) | [🇬🇧 English]

A modern, desktop-based Python application designed to instantly organize messy directories and eliminate duplicate files with a single click. It features a native Graphical User Interface (GUI) and cryptographic file deduplication.

---

## ✨ Features

- **Native Desktop GUI**: Powered by `tkinter`. Integrated with a native **"Browse Folder"** directory picker for a seamless, mouse-driven user experience. No more terminal commands!
- **Smart Deduplication (Core Feature)**: Uses **MD5 cryptographic hashing** to read file fingerprints byte-by-byte via a stream buffer (`8192` bytes). It catches duplicates even if they have completely different filenames.
- **Safety First**: Duplicates are safely isolated into a dedicated `/duplicates` directory instead of being deleted permanently.

---

## 🛠️ Supported Formats

| Category | Supported Extensions | Target Folder |
| :--- | :--- | :--- |
| 🎵 **Audio** | `.mp3`, `.flac`, `.wav`, `.m4a` | `/audio` |
| 🎬 **Video** | `.mp4`, `.mkv`, `.avi`, `.mov` | `/video` |
| 🖼️ **Picture** | `.jpg`, `.jpeg`, `.png`, `.gif` | `/picture` |
| 👯 **Duplicates** | *Content Identical* | `/duplicates` |

---

## 🚀 How to Run

### Prerequisites
Make sure you have Python 3.x installed on your system. This software relies completely on Python's standard libraries—**no external pip installations required!**

### Steps
1. Clone or download this repository to your local machine.
2. Open your terminal/command prompt and navigate to the project directory.
3. Run the English GUI version:
   ```bash
   python app_en.py