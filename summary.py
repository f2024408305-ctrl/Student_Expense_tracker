import tkinter as tk
from tkinter import ttk
import database

def open_summary_window():
    # Fetch live math calculations from the database
    total_spent, breakdown = database.fetch_expense_summary()

    # Create the popup window
    summary_win = tk.Toplevel()
    summary_win.title("Financial Insights Summary")
    summary_win.geometry("400x450")
    summary_win.configure(bg="#f4f6f9")
    summary_win.resizable(False, False)

    # Title Banner
    header = tk.Label(
        summary_win, 
        text="📊 Spending Insights", 
        font=("Arial", 16, "bold"), 
        bg="#2c3e50", 
        fg="white", 
        pady=10
    )
    header.pack(fill=tk.X)

    # Total Budget Metric Card
    card_frame = tk.Frame(summary_win, bg="white", bd=1, relief="solid", padx=15, pady=15)
    card_frame.pack(pady=20, padx=20, fill=tk.X)

    total_lbl = tk.Label(card_frame, text="TOTAL AMOUNT SPENT", font=("Arial", 10, "bold"), bg="white", fg="#7f8c8d")
    total_lbl.pack()

    # Formats the number cleanly to 2 decimal places with currency formatting
    amount_lbl = tk.Label(card_frame, text=f"${total_spent:,.2f}", font=("Arial", 24, "bold"), bg="white", fg="#e74c3c")
    amount_lbl.pack(pady=5)

    # Category Breakdown Header
    breakdown_lbl = tk.Label(summary_win, text="Breakdown By Category", font=("Arial", 12, "bold"), bg="#f4f6f9", fg="#2c3e50")
    breakdown_lbl.pack(anchor="w", padx=20, pady=(10, 5))

    # Grid Display Container
    list_frame = tk.Frame(summary_win, bg="#f4f6f9")
    list_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

    if not breakdown:
        empty_lbl = tk.Label(list_frame, text="No expense data found to analyze.", font=("Arial", 10, "italic"), bg="#f4f6f9", fg="#95a5a6")
        empty_lbl.pack(pady=20)
    else:
        # Loop through database calculations and build clean rows
        for category, amt in breakdown:
            row = tk.Frame(list_frame, bg="#f4f6f9")
            row.pack(fill=tk.X, pady=6)

            cat_name = tk.Label(row, text=category, font=("Arial", 11), bg="#f4f6f9", fg="#34495e", width=15, anchor="w")
            cat_name.pack(side=tk.LEFT)

            cat_amt = tk.Label(row, text=f"${amt:,.2f}", font=("Arial", 11, "bold"), bg="#f4f6f9", fg="#2c3e50", anchor="e")
            cat_amt.pack(side=tk.RIGHT)

    # Close Action Button
    close_btn = ttk.Button(summary_win, text="Close Insights", command=summary_win.destroy)
    close_btn.pack(pady=15)