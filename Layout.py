import tkinter as tk
from tkinter import ttk

# Initialize main window
root = tk.Tk()
root.title("App Tabs")
root.geometry("400x600")

# Tab colors
ACTIVE_COLOR = "#8B1538"
INACTIVE_COLOR = "#B8860B"
BG_COLOR = "#FDF5E6"
TAB_HEIGHT = 80

# Frames for each tab
home_frame = tk.Frame(root, bg="white")
timeline_frame = tk.Frame(root, bg="white")
locations_frame = tk.Frame(root, bg="white")
capture_frame = tk.Frame(root, bg="white")
music_frame = tk.Frame(root, bg="white")

frames = [home_frame, timeline_frame, locations_frame, capture_frame, music_frame]

for f in frames:
    f.place(relx=0, rely=0, relwidth=1, relheight=0.9)

# Sample content
tk.Label(home_frame, text="Home Screen", font=("Arial", 20)).pack(expand=True)
tk.Label(timeline_frame, text="Timeline Screen", font=("Arial", 20)).pack(expand=True)
tk.Label(locations_frame, text="Locations Screen", font=("Arial", 20)).pack(expand=True)
tk.Label(capture_frame, text="Capture Screen", font=("Arial", 20)).pack(expand=True)
tk.Label(music_frame, text="Music Screen", font=("Arial", 20)).pack(expand=True)

# Tab buttons container
tab_bar = tk.Frame(root, bg=BG_COLOR, height=TAB_HEIGHT)
tab_bar.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)

# Tab button click handler
def show_frame(index):
    for i, f in enumerate(frames):
        f.lift()  # Bring the selected frame to top
        btns[i].config(fg=ACTIVE_COLOR if i == index else INACTIVE_COLOR)

# Tab buttons
btns = []
labels = ["Home", "Timeline", "Locations", "Capture", "Music"]
for i, label in enumerate(labels):
    btn = tk.Button(tab_bar, text=label, fg=INACTIVE_COLOR, bg=BG_COLOR,
                    font=("Arial", 10, "bold"), bd=0, command=lambda i=i: show_frame(i))
    btn.pack(side="left", expand=True, fill="both")
    btns.append(btn)

# Show default tab
show_frame(0)

root.mainloop()
