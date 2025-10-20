import tkinter as tk

def create_class_frame(root, go_to_next_frame_callback):
    
    def choose_fighter():
        go_to_next_frame_callback("Fighter")
    def choose_wizard():
        go_to_next_frame_callback("Wizard")
    def choose_rogue():
        go_to_next_frame_callback("Rogue")
    
    frame = tk.Frame(root)

    # Welcome label
    welcome_label = tk.Label(frame, text="Choose a Class Below:", font=("Arial", 14))
    welcome_label.pack(pady=10)

    # Create Buttons for player to click
    fighter_button = tk.Button(frame, text="Fighter", command=choose_fighter)
    wizard_button = tk.Button(frame, text="Wizard", command=choose_wizard)
    rogue_button = tk.Button(frame, text="Rogue", command=choose_rogue)

    fighter_button.pack(pady=5)
    wizard_button.pack(pady=5)
    rogue_button.pack(pady=5)

    return frame