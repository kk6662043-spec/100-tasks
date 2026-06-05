import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import markdown

def update_preview(event=None):
    html = markdown.markdown(editor.get("1.0", tk.END))
    preview.delete("1.0", tk.END)
    preview.insert(tk.END, html)

root = tk.Tk()
root.title("Markdown Previewer")
root.geometry("800x400")

# Markdown editor
editor = ScrolledText(root, wrap="word")
editor.pack(side="left", fill="both", expand=True)

# Preview area
preview = ScrolledText(root, wrap="word")
preview.pack(side="right", fill="both", expand=True)

editor.bind("<KeyRelease>", update_preview)

root.mainloop()