import tkinter as tk
from tkinter import messagebox
import instaloader

def download():
    username = entry.get()

    if not username:
        messagebox.showerror("Error", "Enter username")
        return

    try:
        loader = instaloader.Instaloader()
        loader.download_profile(
            username,
            profile_pic=True,
            posts=True
        )

        messagebox.showinfo(
            "Success",
            "Download Completed"
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            str(e)
        )

root = tk.Tk()
root.title("Instagram Image Downloader")
root.geometry("400x200")

tk.Label(
    root,
    text="Instagram Username"
).pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack()

tk.Button(
    root,
    text="Download Images",
    command=download
).pack(pady=20)

root.mainloop()