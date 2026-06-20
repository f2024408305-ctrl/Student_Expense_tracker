# Dashboard Module
print("Dashboard Loaded")

from tkinter import *
from tkinter import ttk
import database
from view_expense import open_view_expenses_window
from add_expense import open_add_expense_window
import summary
import time

def open_add_expense():
    open_add_expense_window(root)

def open_view_expense():
    open_view_expenses_window(root)

def open_summary():
    summary.open_summary_window()

root = Tk()
root.title("Student Expense Tracker")
root.geometry("550x460")
root.configure(bg="#eef1f7")  # Soft neutral background

# Activates and sets up the SQLite tables when the app boots
database.initialize_db()

# 🏢 Title Banner Area
header_frame = Frame(root, bg="#1f2a44", height=80)
header_frame.pack(fill=X)

title = Label(
    header_frame,
    text="🎓 Student Expense Tracker",
    font=("Arial", 18, "bold"),
    bg="#1f2a44",
    fg="white"
)
title.pack(pady=20)

# 🎴 Navigation Card Container
menu_frame = Frame(root, bg="white", bd=0, highlightbackground="#d7dde5",
                    highlightthickness=1, padx=20, pady=20)
menu_frame.pack(pady=30, padx=30, fill=BOTH, expand=True)

# Define clean base styles for the buttons
btn_config = {
    "font": ("Arial", 11, "bold"),
    "fg": "white",
    "width": 18,
    "height": 2,
    "bd": 0,
    "cursor": "hand2",
    "activeforeground": "white",
}

# Each button: (normal color, hover color)
button_specs = [
    ("➕ Add Expense", "#27ae60", "#2ecc71", open_add_expense, 0, 0),
    ("📋 View Expenses", "#2980b9", "#3498db", open_view_expense, 0, 1),
    ("📊 View Summary", "#8e44ad", "#9b59b6", open_summary, 1, 0),
    ("❌ Exit System", "#c0392b", "#e74c3c", root.destroy, 1, 1),
]

def add_hover_effect(button, normal_color, hover_color):
    button.bind("<Enter>", lambda e: button.configure(bg=hover_color))
    button.bind("<Leave>", lambda e: button.configure(bg=normal_color))

# 🎛️ 2x2 Grid Layout Mapping, now with hover feedback
for text, normal_color, hover_color, command, row, col in button_specs:
    btn = Button(menu_frame, text=text, bg=normal_color, command=command, **btn_config)
    btn.grid(row=row, column=col, padx=15, pady=15)
    add_hover_effect(btn, normal_color, hover_color)

# Center the grid rows/columns inside the menu card frame
menu_frame.grid_columnconfigure(0, weight=1)
menu_frame.grid_columnconfigure(1, weight=1)
menu_frame.grid_rowconfigure(0, weight=1)
menu_frame.grid_rowconfigure(1, weight=1)

# 🕒 Footer Status Bar with a live clock
footer_frame = Frame(root, bg="#1f2a44", height=28)
footer_frame.pack(fill=X, side=BOTTOM)

clock_label = Label(footer_frame, text="", font=("Arial", 9), bg="#1f2a44", fg="#cbd5e1")
clock_label.pack(pady=4)

def update_clock():
    clock_label.config(text=time.strftime("%A, %d %B %Y  |  %H:%M:%S"))
    root.after(1000, update_clock)

update_clock()

root.mainloop()
