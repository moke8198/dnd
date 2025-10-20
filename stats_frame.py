import tkinter as tk

def create_stats_frame(root, chosen_class, go_to_next_frame_callback):
    """
    Creates the stats screen for the character.
    
    Parameters:
    - root: Tk root window
    - chosen_class: string, the class the player chose
    - go_to_next_frame_callback: function to call when the user confirms stats
    
    Returns:
    - frame: the Tkinter Frame object
    """
    frame = tk.Frame(root)
    
    # Top label showing chosen class
    class_label = tk.Label(frame, text=f"You have chosen {chosen_class}", font=("Arial", 14))
    class_label.pack(pady=10)
    
    # Points remaining
    points_remaining = tk.IntVar(value=20)
    points_label = tk.Label(frame, text=f"Points remaining: {points_remaining.get()}", font=("Arial", 12))
    points_label.pack(pady=5)
    
    # Stats dictionary
    stats = {
        "STR": tk.IntVar(value=8),
        "DEX": tk.IntVar(value=8),
        "CON": tk.IntVar(value=8),
        "INT": tk.IntVar(value=8),
        "WIS": tk.IntVar(value=8),
        "CHA": tk.IntVar(value=8)
    }
    
    # Stats grid
    stats_frame = tk.Frame(frame)
    stats_frame.pack(pady=10)
    
    for i, stat in enumerate(stats.keys()):
        # Stat label
        tk.Label(stats_frame, text=stat, width=5).grid(row=i, column=0)
        
        # Stat value
        tk.Label(stats_frame, textvariable=stats[stat], width=3).grid(row=i, column=1)
        
        # "+" button
        def make_increase(s=stat):
            def increase():
                if stats[s].get() < 18 and points_remaining.get() > 0:
                    stats[s].set(stats[s].get() + 1)
                    points_remaining.set(points_remaining.get() - 1)
                    points_label.config(text=f"Points remaining: {points_remaining.get()}")
            return increase
        
        tk.Button(stats_frame, text="+", command=make_increase()).grid(row=i, column=2)
        
        # "-" button
        def make_decrease(s=stat):
            def decrease():
                if stats[s].get() > 8:
                    stats[s].set(stats[s].get() - 1)
                    points_remaining.set(points_remaining.get() + 1)
                    points_label.config(text=f"Points remaining: {points_remaining.get()}")
            return decrease
        
        tk.Button(stats_frame, text="-", command=make_decrease()).grid(row=i, column=3)
    
    # Confirm button to go to the next frame
    def confirm_stats():
        final_stats = {stat: var.get() for stat, var in stats.items()}
        go_to_next_frame_callback(frame, final_stats)
    
    tk.Button(frame, text="Confirm", command=confirm_stats, font=("Arial", 12)).pack(pady=15)
    
    return frame
