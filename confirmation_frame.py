import tkinter as tk

def create_confirmation_frame(root, player_name, chosen_class, final_stats):
    frame = tk.Frame(root)

    # Header label
    tk.Label(frame, text="Character Confirmation", font=("Arial", 14)).pack(pady=10)

    # Show player name and chosen class
    tk.Label(frame, text=f"Name: {player_name}", font=("Arial", 12)).pack()
    tk.Label(frame, text=f"Class: {chosen_class}", font=("Arial", 12)).pack(pady=5)

    # Show stats
    stats_text = "\n".join([f"{stat}: {value}" for stat, value in final_stats.items()])
    tk.Label(frame, text=stats_text, font=("Arial", 12)).pack(pady=5)

    # Button to save character to TXT
    def save_to_file():
        with open("character.txt", "w") as f:
            f.write(f"Name: {player_name}\n")
            f.write(f"Class: {chosen_class}\n")
            f.write("Stats:\n")
            for stat, value in final_stats.items():
                f.write(f"{stat}: {value}\n")
        for child in frame.winfo_children():
            if isinstance(child, tk.Label) and child.cget("text").startswith("Saved to"):
                child.destroy()
        tk.Label(frame, text="Saved to character.txt!", font=("Arial", 12), fg="green").pack(pady=5)

    tk.Button(frame, text="Save to File", command=save_to_file, font=("Arial", 12)).pack(pady=10)

    return frame