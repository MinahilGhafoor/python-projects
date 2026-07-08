from colorama import Fore, Style
from pyfiglet import *

COLORS  = [Fore.CYAN, Fore.GREEN, Fore.YELLOW, Fore.MAGENTA]

CYAN = Fore.CYAN
GREEN = Fore.GREEN
RESET = Style.RESET_ALL
YELLOW = Fore.YELLOW
MAGENTA = Fore.MAGENTA

def figlet(text):
    return figlet_format(text)