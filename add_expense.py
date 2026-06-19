import tkinter as tk
from tkinter import ttk
from tkinter import messagebox  
import database  # Connects directly to your database script!

def open_add_expense_window(parent_window):
    """Creates a popup window to input and save an expense."""
    
    # 1. Create a child popup window linked to the dashboard
    add_win = tk.Toplevel(parent_window)
    add_win.title("Add New Expense")
    add_win.geometry("320x460")  # 👈 Expanded height from 400 to 460 to comfortably fit the dynamic input box
    
    # Freeze interaction with the main dashboard until this window closes
    add_win.grab_set()

    # 2. Form Layout (Labels & Entry Fields)
    tk.Label(add_win, text="STUDENT NAME", font=("Arial", 10, "bold")).pack(pady=5)
    title_entry = tk.Entry(add_win, width=30)
    title_entry.pack(pady=5)

    tk.Label(add_win, text="Amount (PKR):", font=("Arial", 10, "bold")).pack(pady=5)
    amount_entry = tk.Entry(add_win, width=30)
    amount_entry.pack(pady=5)

    tk.Label(add_win, text="Category:", font=("Arial", 10, "bold")).pack(pady=5)
    
    category_var = tk.StringVar()  # 👈 Added to cleanly track combobox changes
    category_dropdown = ttk.Combobox(
        add_win, 
        textvariable=category_var, 
        values=["Food", "Rent", "Utilities", "Entertainment", "Other"], 
        width=27, 
        state="readonly"  # Enforces strict dropdown tracking
    )
    category_dropdown.pack(pady=5)

    # 3. Dynamic UI Hidden elements (Created but not packed yet)
    other_label = tk.Label(add_win, text="Specify Custom Category:", font=("Arial", 9, "italic"), fg="#555555")
    other_entry = tk.Entry(add_win, width=30)

    # ========================================================
    # 🔄 DYNAMIC TOGGLE INTERACTION LOGIC
    # ========================================================
    def check_category_selection(event):
        """Monitors combobox and reveals custom input field if 'Other' is picked."""
        if category_var.get() == "Other":
            # Place the specific input fields right below the dropdown, above the save button
            other_label.pack(pady=(5, 0))
            other_entry.pack(pady=5)
        else:
            # Pluck the widgets out of the layout instantly if another category is clicked
            other_label.pack_forget()
            other_entry.pack_forget()
            other_entry.delete(0, tk.END)  # Clear any text inside if they back out

    # Bind the dropdown choice event to our new layout detector function
    category_dropdown.bind("<<ComboboxSelected>>", check_category_selection)

    # 4. Form Processing Logic
    def handle_save():
        title = title_entry.get().strip()
        amount_raw = amount_entry.get().strip()
        selected_category = category_var.get()

        # Input Validation: Prevent empty fields
        if not title or not amount_raw or not selected_category:
            messagebox.showwarning("Validation Error", "All fields are required!", parent=add_win)
            return

        # Handle "Other" specificity rule extraction
        if selected_category == "Other":
            custom_spec = other_entry.get().strip()
            if not custom_spec:
                messagebox.showwarning("Validation Error", "Please specify the 'Other' category details!", parent=add_win)
                return
            final_category = custom_spec  # Override the keyword "Other" with what they wrote!
        else:
            final_category = selected_category

        # Input Validation: Ensure amount is numeric
        try:
            amount = float(amount_raw)
        except ValueError:
            messagebox.showerror("Input Error", "Amount must be a valid number!", parent=add_win)
            return

        # Automatically capture today's date
        from datetime import date
        today = date.today().strftime("%Y-%m-%d")

        # Send data straight to your database layer! 🚀
        database.add_expense(title, amount, final_category, today)
        
        # Confirmation popup & close window cleanly
        messagebox.showinfo("Success", "Expense added successfully!", parent=add_win)
        add_win.destroy()

    # 5. Save Button
    save_btn = tk.Button(add_win, text="Save Expense", command=handle_save, bg="#2ecc71", fg="white", width=15, font=("Arial", 10, "bold"))
    save_btn.pack(pady=25)