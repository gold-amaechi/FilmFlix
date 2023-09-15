import sqlite3 as sql
from flask import Flask, render_template
import addFilmsFlask, deleteFilmsFlask, readFilmsFlask, updateFilmsFlask, reportsFlask

app = Flask(__name__)

def menuFiles():
    with open("mainMenu.txt") as mainMenuText:
      userMainMenu = mainMenuText.read()
    with open("filmMenu.txt") as filmMenu:
      userMenu = filmMenu.read()
    with open("reportOptions.txt") as reportMenu:
      userReport = reportMenu.read()

    return userMainMenu, userMenu, userReport

def mainMenuOptions():
    options = 0
    optionsList = ["1", "2", "3"]

    userChoices = menuFiles()

    while options not in optionsList:
        print(userChoices[0])

        options = input("Enter a number from the Main Menu above: ")
        if options not in optionsList:
            print(f"{options} is not a valid number")
    return options

def filmMenuOptions():
    options = 0
    optionsList = ["1", "2", "3", "4", "5"]

    userChoices = menuFiles()

    while options not in optionsList:
        print(userChoices[1])

        options = input("Enter a number from the Film Menu above: ")
        if options not in optionsList:
            print(f"{options} is not a valid number")
    return options

def reportMenuOptions():
    options = 0
    optionsList = ["1", "2", "3", "4", "5"]

    userChoices = menuFiles()

    while options not in optionsList:
        print(userChoices[2])

        options = input("Enter a number from the Report Menu above: ")
        if options not in optionsList:
            print(f"{options} is not a valid number")
    return options


mainPage = True
while mainPage:
    mainMenu = mainMenuOptions()

    if mainMenu == "1":
      filmOptionsActions = True
      while filmOptionsActions:
          filmMenu = filmMenuOptions()
          if filmMenu == "1":
              addFilmsFlask.add_records()
          elif filmMenu == "2":
              deleteFilmsFlask.delete_record()
          elif filmMenu == "3":
              updateFilmsFlask.update_record()
          elif filmMenu == "4":
              readFilmsFlask.print_record()
          else:
              filmOptionsActions = False
              input("Press Enter to quit the film sub menu")
    elif mainMenu == "2":
        reportsOptionsAction = True
        while reportsOptionsAction:
            reportsMenu = reportMenuOptions()
            if reportsMenu == "1":
                reportsFlask.reports()
            elif reportsMenu == "2":
                reportsFlask.search_genre()
            elif reportsMenu == "3":
                reportsFlask.search_year()
            elif reportsMenu == "2":
                reportsFlask.search_rating()
            else:
                reportsOptionsAction = False
                input("Press Enter to quit the report sub menu")
    else:
        mainPage = False
input("Press Enter to quit the Film app")
    
if __name__=="__main__":
    app.run(debug=True)

    