# Dashboard Module
print("Dashboard Loaded")

from tkinter import *

def open_add_expense():
    print("Add Expense Module")

def open_view_expense():
    print("View Expense Module")

def open_summary():
    print("Summary Module")

root = Tk()
root.title("Student Expense Tracker")
root.geometry("500x400")

title = Label(root, text="Student Expense Tracker", font=("Arial", 18))
title.pack(pady=20)

btn_add = Button(root, text="Add Expense", width=20, command=open_add_expense)
btn_add.pack(pady=10)

btn_view = Button(root, text="View Expenses", width=20, command=open_view_expense)
btn_view.pack(pady=10)

btn_summary = Button(root, text="Summary", width=20, command=open_summary)
btn_summary.pack(pady=10)

btn_exit = Button(root, text="Exit", width=20, command=root.destroy)
btn_exit.pack(pady=10)

root.mainloop()