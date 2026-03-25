import tkinter as tk
from tkinter import messagebox
import random
import os

def roll_dice():
    return random.randint(1, 6)

def save_history(result):
    with open("history.txt", "a") as f:
        f.write(str(result) + "\n")

def view_history():
    try:
        with open("history.txt", "r") as f:
            data = f.read()
            if not data:
                data = "No history available!"
    except FileNotFoundError:
        data = "No history found!"

    win = tk.Toplevel(root)
    win.title("📜 History")
    win.geometry("400x400")

    frame = tk.Frame(win)
    frame.pack(fill="both", expand=True)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")

    text = tk.Text(frame, font=("Arial", 16), yscrollcommand=scrollbar.set)
    text.pack(expand=True, fill="both")

    scrollbar.config(command=text.yview)

    text.insert("1.0", data)
    text.config(state="disabled")

def show_stats():
    try:
        with open("history.txt", "r") as f:
            rolls = [int(line.strip()) for line in f if line.strip()]

        if rolls:
            stats = (
                f"Total Rolls: {len(rolls)}\n\n"
                f"Average: {sum(rolls)/len(rolls):.2f}\n\n"
                f"Highest: {max(rolls)}\n\n"
                f"Lowest: {min(rolls)}"
            )
        else:
            stats = "No data available!"
    except FileNotFoundError:
        stats = "No history found!"

    win = tk.Toplevel(root)
    win.title("📊 Statistics")
    win.geometry("400x300")

    label = tk.Label(
        win,
        text=stats,
        font=("Arial", 16),
        justify="left",
        anchor="w"
    )
    label.pack(padx=20, pady=20, fill="both")

def clear_history():
    with open("history.txt", "w") as f:  # Empty the file without deleting
        f.write("")
    messagebox.showinfo("Clear History", "History has been cleared!")

def get_dice_face(num):
    faces = {
        1: "⚀",
        2: "⚁",
        3: "⚂",
        4: "⚃",
        5: "⚄",
        6: "⚅"
    }
    return faces[num]

def roll_action():
    result = roll_dice()
    dice_label.config(text=get_dice_face(result))
    result_label.config(text=f"You rolled: {result}")
    save_history(result)

root = tk.Tk()
root.title("🎲 Dice Rolling Game")
root.geometry("400x500")
root.resizable(False, False)

title_label = tk.Label(root, text="🎲 Dice Game", fg="red", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

dice_label = tk.Label(root, text="⚀", font=("Arial", 100), fg="blue")
dice_label.pack()

result_label = tk.Label(root, text="Click 'Roll Dice' to start!", font=("Arial", 14))
result_label.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=20)
btn_frame.columnconfigure(0, weight=1)
btn_frame.columnconfigure(1, weight=1)

roll_button = tk.Button(btn_frame, text="Roll Dice", width=15, font=("Arial", 12),
                        bg="green", fg="white", command=roll_action)
roll_button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

history_button = tk.Button(btn_frame, text="View History", width=15, font=("Arial", 12),
                           bg="blue", fg="white", command=view_history)
history_button.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

stats_button = tk.Button(btn_frame, text="View Stats", width=15, font=("Arial", 12),
                         bg="hotpink", fg="white", command=show_stats)
stats_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

clear_button = tk.Button(btn_frame, text="Clear History", width=15, font=("Arial", 12),
                         bg="orange", fg="white", command=clear_history)
clear_button.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

exit_button = tk.Button(root, text="Exit", width=15, font=("Arial", 12),
                        bg="red", fg="white", command=root.quit)
exit_button.pack(pady=10)

root.mainloop()