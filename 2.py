import tkinter as tk

root = tk.Tk()
root.title("Login")
root.geometry("250x150")

tk.Label(root, text="Username").pack()
username = tk.Entry(root)
username.pack()

tk.Label(root, text="Password").pack()
password = tk.Entry(root, show="*")
password.pack()

tk.Button(root, text="Login").pack(pady=10)

root.mainloop()