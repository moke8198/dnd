# main.py
import tkinter as tk
from name_frame import create_name_frame
from class_frame import create_class_frame
from stats_frame import create_stats_frame
from confirmation_frame import create_confirmation_frame

# Create main window
window = tk.Tk()
window.title("D&D Character Creator")

player_name = ""
selected_class = ""

# Placeholder for next frame function
def show_class_frame(name):
    global player_name
    player_name = name
    frame_name.pack_forget()
    frame_class.pack()

def show_stats_frame(chosen_class):
    global selected_class
    selected_class = chosen_class
    frame_class.pack_forget()
    frame_stats = create_stats_frame(window, chosen_class, go_to_next_frame_callback=show_confirmation_frame)
    frame_stats.pack()

def show_confirmation_frame(frame_stats, final_stats):
    frame_stats.pack_forget()
    frame_confirmation = create_confirmation_frame(window, player_name, selected_class, final_stats)
    frame_confirmation.pack()


# show the order of frames-name-class-stats
frame_name = create_name_frame(window, go_to_next_frame_callback=show_class_frame)
frame_class = create_class_frame(window, go_to_next_frame_callback=show_stats_frame)

# these are the frames
frame_class.pack_forget()  # hide it initially
frame_name.pack()

# Start the GUI
window.mainloop()