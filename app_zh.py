from pathlib import Path
import shutil
import hashlib       
import tkinter as tk 
from tkinter import filedialog, messagebox

# ==========================================
# 🧠 核心算法区：计算文件绝对指纹（MD5）
# ==========================================
def calculate_file_hash(file_path):
    """
    读取文件内容，返回唯一的 MD5 16进制字符串作为文件指纹
    """
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        while content := f.read(8192):
            hasher.update(content)
    return hasher.hexdigest()

# ==========================================
# 🎨 交互与逻辑区：当用户点击“开始智能整理”时触发
# ==========================================
def run_classifier_action():
    # 1. 动态获取用户在输入框里选择的路径
    raw_path = path_entry.get()
    folder = Path(raw_path.strip())
    
    # 2. 容错校验：如果路径为空或者文件夹不存在，弹窗报错并拦截
    if not raw_path or not folder.exists():
        messagebox.showerror("错误", "输入的文件夹路径无效或不存在，请重新选择！")
        return

    # 3. 初始化各类型文件计数器
    audio_count = 0
    video_count = 0
    picture_count = 0
    duplicate_count = 0  # 重复文件计数器

    # 4. 动态定义目标文件夹路径（包含重复文件归纳夹）
    audio_dir = folder / '音频'
    video_dir = folder / '视频'
    picture_dir = folder / '图片'
    duplicate_dir = folder / '重复文件归类' 

    # 自动创建这些文件夹
    audio_dir.mkdir(exist_ok=True)
    video_dir.mkdir(exist_ok=True)
    picture_dir.mkdir(exist_ok=True)
    duplicate_dir.mkdir(exist_ok=True)    

    # 5. 定义常见后缀匹配规则
    audio_exts = ['.mp3', '.flac', '.wav', '.m4a']
    video_exts = ['.mp4', '.mkv', '.avi', '.mov']
    picture_exts = ['.jpg', '.jpeg', '.png', '.gif']

    # 声明一个空集合，作为数字指纹的记账本
    seen_hashes = set()

    # 6. 开始遍历文件夹并进行核心拦截与归类
    for file in folder.iterdir():
        # 确保只处理文件，跳过刚才新建的那些目标文件夹
        if file.is_file():
            
            # 🛡️ 【核心去重拦截】优先计算指纹
            file_hash = calculate_file_hash(file)
            
            if file_hash in seen_hashes:
                # 指纹已存在，说明内容完全重复，直接移入重复归类夹
                shutil.move(file, duplicate_dir)
                duplicate_count += 1
            else:
                # 新文件，先记录指纹账本，再按照后缀分类
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

    # 7. 整理结束，弹出中文结果通知窗口
    result_message = (
        f"✨ 整理完成！本次归档数据统计如下：\n\n"
        f"🎵 音频文件: {audio_count} 个\n"
        f"🎬 视频文件: {video_count} 个\n"
        f"🖼️ 图片文件: {picture_count} 个\n"
        f"👯 重复文件: {duplicate_count} 个" 
    )
    messagebox.showinfo("提示", result_message)


# ==========================================
# 📂 交互事件：点击调用本地浏览器选择文件夹
# ==========================================
def select_folder_action():
    selected_dir = filedialog.askdirectory()
    if selected_dir:
        path_entry.delete(0, tk.END)  
        path_entry.insert(0, selected_dir)  


# ==========================================
# 🚀 软件主窗口布局初始化
# ==========================================
root = tk.Tk()
root.title("白猫智能文件整理器 v2.0")
root.geometry("450x220")

title_label = tk.Label(root, text="请选择您想要整理的文件夹路径:", pady=10)
title_label.pack()

path_entry = tk.Entry(root, width=50)
path_entry.pack(pady=5)

browse_btn = tk.Button(root, text="浏览文件夹", command=select_folder_action)
browse_btn.pack(pady=5)

start_btn = tk.Button(root, text="🚀 开始智能整理", command=run_classifier_action, bg="green", fg="white", pady=5)
start_btn.pack(pady=15)

root.mainloop()