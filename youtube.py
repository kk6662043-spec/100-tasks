import tkinter as tk
from tkinter import messagebox
import yt_dlp

def download_video():
    url = url_entry.get().strip()

    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return

    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        messagebox.showinfo("Success", "Video downloaded successfully!")

    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("500x200")

title = tk.Label(root, text="YouTube Video Downloader", font=("Arial", 16))
title.pack(pady=10)

url_entry = tk.Entry(root, width=60)
url_entry.pack(pady=10)

download_btn = tk.Button(root, text="Download Video", command=download_video)
download_btn.pack(pady=10)

root.mainloop()