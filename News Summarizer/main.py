import requests
from dotenv import load_dotenv
import os
from rich.console import Console
from rich.table import Table
#***************************************************************

console = Console()

#******************************************************************
load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://newsapi.org/v2/top-headlines"

CATEGORIES = ["business", "entertainment", "health", "science", "sports", "technology"]

def go():
     while True:
          choice = input("Enter y to browse or n to quit. (y/n):   ").lower().strip()

          if choice == "n":
               return False
          elif choice == "y":
               return True
          else:
               print("Invalid choice.")
               continue

def get_category():
    for i, cat in enumerate(CATEGORIES, start=1):
            print(f"{i}. {cat}")

    while True:

            choice = input("Enter your choice:  ").strip()

            if choice.isdigit():
                choice = int(choice) - 1

                if 0 <= choice < len(CATEGORIES):
                    return CATEGORIES[choice]
                
                else:
                    print("Invalid Choice. Try Again")
                    continue

            else:
                print("Enter a valid number.")
                continue


def get_news(category):
    params = {"category" : category, "apiKey" : API_KEY, "country" : "us", "pageSize" : 5}
    response = requests.get(BASE_URL, params)
    return response.json()

def display_news(data):
    table = Table()

    columns = ["📰 Title", "📡 Source", "📝 Description", "🕐 Published"]

    for i in columns:
        table.add_column(i)


    for i in data["articles"]:
        table.add_row(i["title"], i["source"]["name"], i["description"], i["publishedAt"])


    console.print(table)


def main():
    while True:
        if go():
            category = get_category()
            articles = get_news(category)

            if articles.get("cod") == 200:
                print(f"Error! Message : {articles.get("message")}")
            else:
                display_news(articles)
        else:
             print("Bye")
             quit()


main()