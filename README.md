# 🎓 Student Expense Tracker

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Database](https://img.shields.io/badge/database-SQLite3-lightgrey.svg)](https://www.sqlite.org/)
[![GUI Framework](https://img.shields.io/badge/UI-Tkinter%20%2F%20ttk-orange.svg)](https://docs.python.org/3/library/tkinter.html)

A modular, lightweight, desktop-based GUI application engineered in Python leveraging **Tkinter (ttk)** and **SQLite3**. Built specifically with a student-centric workflow in mind, this software provides localized financial data persistence, dynamic ledger views, and real-time analytical spending breakdowns without requiring an active internet connection.

---

## 📸 Application Gallery

| 📊 1. Main Dashboard Hub | 📥 2. Add Expense Engine | 🗂️ 3. Live Ledger Grid | 📈 4. Financial Insights |
| :---: | :---: | :---: | :---: |
| `![](./screenshots/dashboard.png)` | `![](./screenshots/add_expense.png)` | `![](./screenshots/view_expenses.png)` | `![](./screenshots/summary.png)` |
| Central operational terminal | Input engine with validation | Dynamic database table grid | Statistical spending breakdown |

---

## ✨ System Features & Capabilities

* **🎛️ Central Navigation Terminal (`dashboard.py`):** Acts as the primary application coordinator, spawning independent lifecycle-managed child frames for data input and viewing.
* **📥 Secure Input Engine (`add_expense.py`):** Features a stylized input form utilizing the `tkcalendar` module for clean chronological data picking. Built with explicit client-side form validation.
* **🗂️ Dynamic Data Ledger (`view_expense.py`):** Displays stored transactions cleanly inside a Tkinter `Treeview` layout engine. Auto-refreshes records chronologically from newest to oldest.
* **🧮 Automated Metrics Aggregator (`summary.py`):** Runs relational SQL analytics on the backend to dynamically render overall spending sums and categorize expenditures with accurate percentage tracking.
* **🔒 Injection-Proof Storage (`database.py`):** Utilizes parameterized SQLite statements to enforce system security and completely neutralize SQL Injection (SQLi) vulnerabilities.

---

## 📐 Architecture & Structural Flow

The application strictly implements the **Separation of Concerns (SoC)** principle, completely dividing data operations, UI layouts, and state processing routines into specific modules:

```text
       ┌────────────────────────────────────────────────────────┐
       │                   dashboard.py (Hub)                   │
       └───────────────┬────────────────────────┬───────────────┘
                       │                        │
       ┌───────────────┴────┐              ┌────┴───────────────┐
       │   add_expense.py   │              │  view_expense.py   │
       └───────────────┬────┘              └────┬───────────────┘
                       │                        │
                       │  Invokes Database CRUD │  Requests Live Rows
                       ▼                        ▼
┌────────────────────────────────────────────────────────────────────────┐
│                          database.py (Engine)                          │
├────────────────────────────────────────────────────────────────────────┤
│  • initialize_db()      • add_expense()      • fetch_all_expenses()   │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │
                                   ▼
                       [ expenses.db (SQLite3) ]


🛠️ Detailed Installation & Local ExecutionSystem
 PrerequisitesPython: Version 3.8 or higher.
Package Manager: pip (standard with Python installations).
Step-by-Step Setup GuideClone the Project
Core:Bash   git clone [https://github.com/f2024408305-ctrl/Student_Expense_tracker.git](https://github.com/f2024408305-ctrl/Student_Expense_tracker.git)
   cd Student_Expense_tracker
Isolate Environment Dependencies (Highly Recommended):Bash   python -m venv venv
   # Activating on Windows:
   .\venv\Scripts\activate
   # Activating on macOS/Linux:
   source venv/bin/activate
Install Framework Dependencies
:Bash   pip install tkcalendar
Launch the Core Application:
Bash   python -m dashboard
🗃️ Relational Database Schema Model
The persistent engine runs natively on SQLite, initializing the following relational framework automatically upon the first boot of the application:
Table Name: expensesColumn NameData Field TypeAttributes & KeysFunctional PurposeidINTEGERPRIMARY KEY AUTOINCREMENTUnique identifier assigned to each transaction entry.
titleTEXTNOT NULLUser-defined label descriptive of the purchase item.amountREALNOT NULLFloat numeric value tracking the financial cost of item.
categoryTEXTNOT NULLTag identifier managing spending classifications.dateTEXTNOT NULLISO-8601 string mapping the calendar execution point.


📂 Production Code Directory MapPlaintextStudent_Expense_tracker/
│
├── screenshots/               # Application UI visual assets for documentation
│   ├── dashboard.png
│   ├── add_expense.png
│   ├── view_expenses.png
│   └── summary.png
│
├── .gitignore                 # Excludes environments, local caches, and active DBs
├── README.md                  # Detailed developer documentation blueprint
│
├── main.py                    # Root bootswrapper target
├── dashboard.py               # Main window shell layout structure
├── add_expense.py             # Form collection window with dropdowns & validation
├── view_expense.py            # Data rendering window containing spreadsheet grid
├── summary.py                 # Analytics generator processing database mathematics
└── database.py                # Database connection orchestrator and CRUD runner

