import os, time

import requests
from replit import db

db.clear()
i=0


def new_joke():
  result = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"})
  joke = result.json()
  return joke

def print_joke(id):
  result = requests.get(f"https://icanhazdadjoke.com/j/{id}", headers={"Accept":"application/json"})
  joke = result.json()
  return joke

try:
  while True:
    time.sleep(3)  # Adding a delay of one second
    os.system("clear")  # Clearing the console screen
    print("🌟Random Joke🌟")  # Printing the title of the system

    choice = input("1: New Joke, 2: Save Joke, 3: Terminate Program 4: Load All Jokes>")

    if choice == "1":
        print("Choice 1")
        joke_data = new_joke()
        joke = joke_data['joke']
        id = joke_data['id']
        print(joke)
        print(id)

    elif choice == "2":
      print("Choice 2")
      db[i]=joke_data['id']
      i+=1

    elif choice == "3":
      print("Program Terminated")

      break
    elif choice == "4":

      if not db.keys():
        print("Database is empty.")
      else:
          for key in db.keys():
            print(print_joke(db[key])["joke"])
    else: 
      print("Wrong input")


except KeyboardInterrupt:
  print("\nProgram exited by user.")
