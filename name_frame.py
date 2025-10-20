# name_frame.py
import tkinter as tk

def create_name_frame(root, go_to_next_frame_callback):
   
    frame = tk.Frame(root)

    # Welcome label
    welcome_label = tk.Label(frame, text="Welcome to the D&D Character Creator!", font=("Arial", 14))
    welcome_label.pack(pady=10)

    # Name prompt
    name_label = tk.Label(frame, text="Enter your character name:")
    name_label.pack()

    # Name entry
    name_entry = tk.Entry(frame)
    name_entry.pack(pady=5)

    # Next button callback
    def on_next():
        player_name = name_entry.get()
        if player_name.strip() == "":
            tk.messagebox.showwarning("Warning", "Please enter a name!")
            return
        go_to_next_frame_callback(player_name)

    # Next button
    next_button = tk.Button(frame, text="Next", command=on_next)
    next_button.pack(pady=10)

    return frame