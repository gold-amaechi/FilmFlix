from connect import *

def add_records():
    filmTitle = input("Enter Film Title: ").title()
    releaseYear = input("Enter Year Film was Released: ")
    filmRating = input("Enter Film Rating system: ").upper()
    filmDuration = input("Enter Duration in minutes: ")
    filmGenre = input("Enter Film Genre: ").title()

    dbCursor.execute("INSERT INTO tblFilms VALUES (NULL,?, ?, ?, ?, ?)", (filmTitle, releaseYear, filmRating, filmDuration, filmGenre))

    dbCon.commit()

    print(f"{filmTitle} inserted into films table")

if __name__ == "__main__":
    add_records()
