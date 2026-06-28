from rich.console import Console
from rich.table import Table
import pandas as pd
from tabulate import tabulate
from color_ama import *
from datetime import datetime
import random
#################################################################
COLOR = random.choice(COLORS)
CSV_FILE = "expenses.csv"
##############################################################
CATEGORIES = ["Food", "Transport", "Utilities", "Entertainment", "Miscellaneous"]
#########################################################################################
console = Console()

###########################################################################################
#**************************************************************************************
def getNotes():
    notes = input("Enter notes: ")
    return notes

def getCategory():
    while True:
        print("Existing Categories: ")
        for count, element in enumerate(CATEGORIES, start = 1):
            print(random.choice(COLORS) + f"{count}. {element}" + RESET)

        choice = input("Enter you choice:  ")

        if choice.isdigit():
            choice = int(choice) - 1
            try:
                category = CATEGORIES[choice]
                return category
            except:
                print("This category does not exist.")
                continue

        else:
            print(Fore.RED + "❌ Please enter a valid number." + Style.RESET_ALL)

def getAmount():
    while True:
        amount = input("Enter amount of expense in dollars: $")

        try:
            amount = float(amount)
            return amount
        except:
            print("Enter valid amount!")




        if amount.isdigit():
            amount = f"${amount}.00"
            return amount
        else:
            print(Fore.RED + "❌ Please enter a valid number." + Style.RESET_ALL)
            continue

def getDate():
    return datetime.now().date()

#***************************************************************************************

#**************************************************************************************
#**************************************************************************************

def read_csv(csv_file_path):
    df = pd.read_csv(csv_file_path)
    df["Category"]= df["Category"].str.strip()
    return df

def saveExpense(date, category, amount, notes):
    try:
        df = read_csv(CSV_FILE)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Date","Category","Amount","Notes"])

    new_row = {"Date" : date,  "Category" : category,  "Amount" : amount, "Notes" : notes}

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index = True)

    df.to_csv(CSV_FILE, index=False)

def get_month():
    while True:
        month = input("Enter a month in number to filter data:  ")
        if month.isdigit():
            month = int(month)
            if month in range(1,13):
                return month
            else:
                print("Invalid month.")
        else:
            print(Fore.RED + "❌ Please enter a valid number." + Style.RESET_ALL)

def get_mode():
    while True:
        mode = input("Want (1. Detailed data, 2. Summary data):  ").strip()
        if mode == "":
            print(COLOR + "You gave no response!" + RESET)
            continue
        
        if mode in MODES:
            return mode
        else:
            print(COLOR + "Invalid mode." + RESET)


def detailed_data_by_month(month):
    table = Table(title="Expenses")
    table.add_column("Date")
    table.add_column("Category")
    table.add_column("Amount")
    table.add_column("Notes")

    df = read_csv(CSV_FILE)

    df = df[pd.to_datetime(df["Date"]).dt.month == month]
    
    for _,row in df.iterrows():
        table.add_row(str(row["Date"]), str(row["Category"]),str(row["Amount"]),str(row["Notes"]))

    console.print(table)

def summarized_data_by_month(month):
    table = Table(title="Expenses")
    df = read_csv(CSV_FILE)
    df = df[pd.to_datetime(df["Date"]).dt.month == month]

    df = df.groupby("Category")["Amount"].sum().reset_index()

    table.add_column("Category")
    table.add_column("Amount")

    for _, row in df.iterrows():
        table.add_row(str(row["Category"]), str(row["Amount"]))
    console.print(table)
MODES = {"1" : detailed_data_by_month, "2": summarized_data_by_month}

#***************************************************************************************
#***************************************************************************************
def addExpense():
    
    date = getDate()
    category = getCategory()
    amount = getAmount()
    notes = getNotes()

    saveExpense(date, category, amount, notes)

def viewSummary():
    df = pd.read_csv(CSV_FILE)
    df.columns = df.columns.str.strip()
    summary = df.groupby("Category")["Amount"].sum().reset_index()

    print(tabulate(summary, headers="keys", tablefmt="fancy_grid"))

def filterByMonth():
    month = get_month()
    mode = get_mode()

    MODES[mode](month)

def exit_app():
    print(COLOR + "GOOOOOOOOOOOD BYE!!!" + RESET)
    quit()


MENU = {"1️⃣  Add Expense" : addExpense,
        
        "2️⃣  View Summary" : viewSummary, 
        "3️⃣  Filter by Month" : filterByMonth, 
        "4️⃣  Exit" : exit_app}


