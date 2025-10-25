import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Sample data
categories = [
    {'id': 'all', 'label': 'All'},
    {'id': 'romantic', 'label': 'Romantic'},
    {'id': 'outdoor', 'label': 'Outdoor'},
    {'id': 'restaurant', 'label': 'Dining'},
    {'id': 'unique', 'label': 'Unique'}
]

venues = [
    {
        'id': 1,
        'name': 'Sunset Beach Pier',
        'category': 'outdoor',
        'rating': 4.8,
        'image': 'https://images.pexels.com/photos/1566837/pexels-photo-1566837.jpeg?auto=compress&cs=tinysrgb&w=400',
        'description': 'Perfect golden hour backdrop for your special moment',
        'duration': '30-45 min',
        'crowd': 'Moderate',
        'tips': 'Best time: 6-7 PM during golden hour'
    },
    {
        'id': 2,
        'name': 'Rose Garden Gazebo',
        'category': 'romantic',
        'rating': 4.9,
        'image': 'https://images.pexels.com/photos/1024993/pexels-photo-1024993.jpeg?auto=compress&cs=tinysrgb&w=400',
        'description': 'Surrounded by beautiful roses and fairy lights',
        'duration': '20-30 min',
        'crowd': 'Low',
        'tips': 'Visit during evening for lights'
    }
]

# Initialize window
root = tk.Tk()
root.title("Locations")
root.geometry("400x600")

# Search bar
search_var = tk.StringVar()
search_entry = tk.Entry(root, textvariable=search_var, font=("Arial", 12))
search_entry.pack(padx=10, pady=10, fill="x")

# Categories frame
categories_frame = tk.Frame(root)
categories_frame.pack(fill="x", padx=10)
selected_category = tk.StringVar(value="all")

def select_category(cat_id):
    selected_category.set(cat_id)
    render_venues()

for cat in categories:
    btn = tk.Radiobutton(
        categories_frame,
        text=cat['label'],
        variable=selected_category,
        value=cat['id'],
        indicatoron=False,
        command=lambda c=cat['id']: select_category(c),
        width=8
    )
    btn.pack(side="left", padx=2, pady=5)

# Scrollable venues frame
canvas = tk.Canvas(root)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Venue cards
venue_widgets = []

def render_venues():
    # Clear previous widgets
    for w in venue_widgets:
        w.destroy()
    venue_widgets.clear()

    query = search_var.get().lower()
    for venue in venues:
        if (selected_category.get() != "all" and venue['category'] != selected_category.get()):
            continue
        if query and query not in venue['name'].lower():
            continue

        frame = tk.Frame(scrollable_frame, bd=1, relief="solid", padx=5, pady=5)
        frame.pack(fill="x", pady=5, padx=5)
        venue_widgets.append(frame)

        # Image
        try:
            response = requests.get(venue['image'])
            img = Image.open(BytesIO(response.content)).resize((100, 60))
            photo = ImageTk.PhotoImage(img)
            img_label = tk.Label(frame, image=photo)
            img_label.image = photo
            img_label.pack(side="left", padx=5)
        except:
            pass

        # Info
        info_frame = tk.Frame(frame)
        info_frame.pack(side="left", fill="both", expand=True)
        tk.Label(info_frame, text=venue['name'], font=("Arial", 12, "bold")).pack(anchor="w")
        tk.Label(info_frame, text=f"Rating: {venue['rating']}").pack(anchor="w")
        tk.Label(info_frame, text=venue['description'], wraplength=250).pack(anchor="w")

# Render initially
render_venues()

# Search functionality
def on_search_change(*args):
    render_venues()

search_var.trace_add("write", on_search_change)

root.mainloop()
