import tkinter as tk

# Initialize main window
root = tk.Tk()
root.title("Camera Overlay UI")
root.geometry("400x700")
root.configure(bg="black")

# Camera container (placeholder for video feed)
camera_container = tk.Frame(root, bg="gray")
camera_container.pack(fill="both", expand=True)

# Camera overlay (transparent effect simulation)
camera_overlay = tk.Frame(camera_container, bg="black")
camera_overlay.place(relwidth=1, relheight=1)

# Close button
close_button = tk.Button(
    camera_overlay,
    text="X",
    fg="white",
    bg="#00000080",  # semi-transparent effect
    font=("Arial", 14, "bold"),
    command=root.destroy
)
close_button.place(relx=0.9, rely=0.08, width=40, height=40)

# Camera controls frame
camera_controls = tk.Frame(camera_overlay, bg="black")
camera_controls.place(relx=0, rely=0.8, relwidth=1, relheight=0.2)

def toggle_capture():
    if capture_button['bg'] == '#8B1538':
        capture_button.config(bg='#FF0000')
    else:
        capture_button.config(bg='#8B1538')

# Control buttons
btn1 = tk.Button(camera_controls, text="Btn1", bg="#00000080", fg="white", width=6, height=3)
btn1.pack(side="left", padx=10, pady=20)

# Capture button
capture_button = tk.Button(
    camera_controls,
    text="Capture",
    bg="#8B1538",
    fg="white",
    width=8,
    height=4,
    command=toggle_capture
)
capture_button.pack(side="left", padx=10, pady=20)

btn2 = tk.Button(camera_controls, text="Btn2", bg="#00000080", fg="white", width=6, height=3)
btn2.pack(side="left", padx=10, pady=20)

root.mainloop()
