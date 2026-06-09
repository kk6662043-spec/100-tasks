from tkinter import *

root = Tk()
root.title("Music Streaming App")
root.geometry("900x600")
root.configure(bg="#121212")

# Header
header = Label(
    root,
    text="🎵 Music Streaming App",
    font=("Arial", 24, "bold"),
    bg="#121212",
    fg="white"
)
header.pack(pady=15)

# Sidebar
sidebar = Frame(root, bg="#1E1E1E", width=200)
sidebar.pack(side=LEFT, fill=Y)

Button(sidebar, text="🏠 Home", width=20).pack(pady=10)
Button(sidebar, text="🔍 Search", width=20).pack(pady=10)
Button(sidebar, text="📚 Library", width=20).pack(pady=10)
Button(sidebar, text="❤️ Favorites", width=20).pack(pady=10)

# Main Content
main = Frame(root, bg="#181818")
main.pack(side=RIGHT, fill=BOTH, expand=True)

Label(
    main,
    text="Trending Songs",
    font=("Arial", 20, "bold"),
    bg="#181818",
    fg="white"
).pack(pady=20)

songs = [
    "Shape of You",
    "Believer",
    "Blinding Lights",
    "Perfect",
    "Levitating"
]

for song in songs:
    frame = Frame(main, bg="#282828")
    frame.pack(fill=X, padx=20, pady=5)

    Label(
        frame,
        text=song,
        font=("Arial", 14),
        bg="#282828",
        fg="white"
    ).pack(side=LEFT, padx=10, pady=10)

    Button(frame, text="▶ Play").pack(side=RIGHT, padx=10)

# Bottom Player
player = Frame(root, bg="#202020", height=80)
player.pack(side=BOTTOM, fill=X)

Label(
    player,
    text="Now Playing: Shape of You",
    bg="#202020",
    fg="white",
    font=("Arial", 12)
).pack(side=LEFT, padx=20)

Button(player, text="⏮").pack(side=RIGHT, padx=5, pady=15)
Button(player, text="⏯").pack(side=RIGHT, padx=5, pady=15)
Button(player, text="⏭").pack(side=RIGHT, padx=20, pady=15)

root.mainloop()