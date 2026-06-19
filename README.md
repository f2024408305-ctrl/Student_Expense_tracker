# 🎓 Student Expense Tracker

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Database](https://img.shields.io/badge/database-SQLite3-lightgrey.svg)](https://www.sqlite.org/)

A modular, desktop-based GUI application built in Python using **Tkinter** and **SQLite3**. Engineered specifically for students, this tracker provides a seamless interface to log daily expenditures, categorize transactions, and view automated spending analytics.

---

## 📸 Application Preview

| Main Dashboard | View Ledger Grid | Expense Insights |
| :---: | :---: | :---: |
| *[Dashboard Preview]* | *[Table Ledger Preview]* | *[Summary Preview]* |
| `![](./screenshots/dashboard.png)` | `![](./screenshots/view_expenses.png)` | `![](./screenshots/summary.png)` |

---

## ✨ Features

* **🗂️ Centralized Dashboard:** Act as an application coordinator managing distinct operational child windows.
* **📥 Smart Input Engine:** Validates data entries, preventing SQL injections via parameterized queries, featuring integrated `tkcalendar` dropdowns.
* **📊 Live Data Grid:** Built using Tkinter's `Treeview` widget, pulling structural records dynamically using descending date orders.
* **🧮 Analytical Summaries:** (In Active Development) Aggregates overall totals and dynamically calculates mathematical percentages across categories.

---

## 📐 System Architecture & Data Flow

The codebase strictly adheres to the **Separation of Concerns (SoC)** design principle, ensuring the UI remains entirely decoupled from data manipulation routines.

```text
┌────────────────────────────────────────────────────────┐
│                   dashboard.py (Hub)                   │
└───────────────┬────────────────────────┬───────────────┘
                │                        │
                ▼                        ▼
     ┌────────────────────┐    ┌────────────────────┐
     │  add_expense.py    │    │  view_expense.py   │
     └──────────┬─────────┘    └─────────┬──────────┘
                │                        │
                │  Invokes functions     │  Requests data
                ▼                        ▼
┌────────────────────────────────────────────────────────┐
│                   database.py (Engine)                 │
├────────────────────────────────────────────────────────┤
│   - initialize_db()       - add_expense()              │
│   - get_connection()      - fetch_all_expenses()       │
└────────────────────────┬───────────────────────────────┘
                         │
                         ▼
             [ expenses.db (SQLite3) ]




🛠️ Installation & Local SetupPrerequisites
Python 3.8 or higher installed on your machine.
Git installed
locally.Step-by-Step Execution

Clone the Remote Repository:Bash   git clone [https://github.com/f2024408305-ctrl/Student_Expense_tracker.git](https://github.com/f2024408305-ctrl/Student_Expense_tracker.git)
   cd Student_Expense_tracker
Initialize and Establish Virtual Environment (Recommended):Bash   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
Install Required Extensions:Bash   pip install tkcalendar
Launch the Engine:Bash   python -m dashboard
🗃️ Database Schema BlueprintThe application manages local data persistence via an auto-generating SQLite database structure:Field ColumnData TypeModifiersDescriptionidINTEGERPRIMARY KEY AUTOINCREMENTUnique record identifiertitleTEXTNOT NULLName/Description of transactionamountREALNOT NULLMonetary spending cost valuecategoryTEXTNOT NULLTarget classification boundarydateTEXTNOT NULLChronological timestamp string
