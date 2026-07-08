from colorama import Style, Fore
from pyfiglet import *
from tabulate import tabulate
import pandas as pd

# COLORS 
RED = Fore.RED
#ORANGE = Fore.ORANGE
MAGENTA = Fore.MAGENTA
CYAN = Fore.CYAN
RESET = Style.RESET_ALL

# FIGLET
def figlet(text):
    return figlet_format(text)


# FIGET AND COLORED TEXT #

print(MAGENTA + figlet("MINAHIL GHAFOOR")+ RESET)

    
# SHOW CSV FILE

def tabulatew():
    df = pd.read_csv("expenses.csv")
    summary = df.groupby("Category")["Amount"].sum().reset_index()

    print(tabulate(summary, headers="keys", tablefmt="fancy_grid"))

tabulatew()