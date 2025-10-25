import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random
import datetime

# Initialize main window
root = tk.Tk()
root.title("Capture Tab")
root.geometry("400x600")

# State variables
is_recording = tk.BooleanVar(value=False)
show_camera = tk.BooleanVar(value=False)
captured_media = []

# Header
header_frame = tk.Frame(root, bg="#8B1538", height=120)
header_frame.pack(fill="x")
tk.Label(header_frame, text="Capture the Moment", font=("Arial", 18, "bold"), fg="white", bg="#8B1538").pack(pady=(20,0))
tk.Label(header_frame, text="Preserve your special memories 📸", font=("Arial", 12), fg="white", bg="#8B1538").pack()

# Permission section
def request_permission():
    show_camera.set(True)
    permission_frame.pack_forget()
    camera_frame.pack(fill="both", expand=True)

permission_frame = tk.Frame(root)
permission_frame.pack(fill="both", expand=True, pady=20)

tk.Label(permission_frame, text="Camera Access Required", font=("Arial", 14, "bold")).pack(pady=10)
tk.Label(permission_frame, text="We need your permission to access the camera so you can capture your special proposal moment", wraplength=300, justify="center").pack(pady=10)
tk.Button(permission_frame, text="Grant Camera Permission", command=request_permission, bg="#8B1538", fg="white").pack(pady=20)

# Camera mock section
camera_frame = tk.Frame(root)

def toggle_recording():
    if not is_recording.get():
        is_recording.set(True)
        record_button.config(text="Stop Recording", bg="#FF0000")
        messagebox.showinfo("Recording", "Simulating recording... 🎥")
    else:
        is_recording.set(False)
        record_button.config(text="Start Recording", bg="#8B1538")
        # Simulate capturing media
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        media_name = f"Video_{len(captured_media)+1} - {timestamp}"
        captured_media.append(media_name)
        render_captured_media()
        messagebox.showinfo("Captured", f"Saved {media_name}")

def flip_camera():
    messagebox.showinfo("Flip Camera", "Simulating camera flip 🔄")

record_button = tk.Button(camera_frame, text="Start Recording", bg="#8B1538", fg="white", command=toggle_recording)
flip_button = tk.Button(camera_frame, text="Flip Camera", bg="#555555", fg="white", command=flip_camera)

record_button.pack(pady=10)
flip_button.pack(pady=10)

# Captured media list
media_frame = tk.Frame(root)
media_frame.pack(fill="both", expand=True, pady=10)

def render_captured_media():
    # Clear previous
    for widget in media_frame.winfo_children():
        widget.destroy()
    tk.Label(media_frame, text="Captured Media:", font=("Arial", 14, "bold")).pack(anchor="w", padx=10)
    for media in captured_media:
        tk.Label(media_frame, text=media, anchor="w").pack(fill="x", padx=20)

# Show camera if permission already granted (for mock)
if show_camera.get():
    permission_frame.pack_forget()
    camera_frame.pack(fill="both", expand=True)

root.mainloop()
