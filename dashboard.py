# Dashboard Module
print("Dashboard Loaded")

from tkinter import *
from tkinter import ttk  
import database  
from view_expense import open_view_expenses_window  
from add_expense import open_add_expense_window    
import summary

def open_add_expense():
    open_add_expense_window(root)

def open_view_expense():
    open_view_expenses_window(root)  

def open_summary():
    summary.open_summary_window()

root = Tk()
root.title("Student Expense Tracker")
root.geometry("550x420")
root.configure(bg="#f4f6f9")  # Clean light gray background

# Activates and sets up the SQLite tables when the app boots
database.initialize_db()

# 🏢 Title Banner Area
header_frame = Frame(root, bg="#2c3e50", height=80)
header_frame.pack(fill=X)

title = Label(
    header_frame, 
    text="🎓 Student Expense Tracker", 
    font=("Arial", 18, "bold"), 
    bg="#2c3e50", 
    fg="white"
)
title.pack(pady=20)

# 🎴 Navigation Card Container
menu_frame = Frame(root, bg="white", bd=1, relief="solid", padx=20, pady=20)
menu_frame.pack(pady=30, padx=30, fill=BOTH, expand=True)

# Define clean styles for the buttons
btn_config = {
    "font": ("Arial", 11, "bold"),
    "fg": "white",
    "width": 18,
    "height": 2,
    "bd": 0,
    "cursor": "hand2"
}

# 🎛️ 2x2 Grid Layout Mapping
# Row 0
btn_add = Button(menu_frame, text="➕ Add Expense", bg="#2ecc71", command=open_add_expense, **btn_config)
btn_add.grid(row=0, column=0, padx=15, pady=15)

btn_view = Button(menu_frame, text="📋 View Expenses", bg="#3498db", command=open_view_expense, **btn_config)
btn_view.grid(row=0, column=1, padx=15, pady=15)

# Row 1
btn_summary = Button(menu_frame, text="📊 View Summary", bg="#9b59b6", command=open_summary, **btn_config)
btn_summary.grid(row=1, column=0, padx=15, pady=15)

btn_exit = Button(menu_frame, text="❌ Exit System", bg="#e74c3c", command=root.destroy, **btn_config)
btn_exit.grid(row=1, column=1, padx=15, pady=15)

# Center the grid rows/columns inside the menu card frame
menu_frame.grid_columnconfigure(0, weight=1)
menu_frame.grid_columnconfigure(1, weight=1)
menu_frame.grid_rowconfigure(0, weight=1)
menu_frame.grid_rowconfigure(1, weight=1)

root.mainloop()