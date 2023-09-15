from connect import *

def reports():
    dbCursor.execute("SELECT * FROM tblFilms ")
    allRecords = dbCursor.fetchall()

    for eachRecord in allRecords:
        print(eachRecord)

def search_genre():
    genreValue = input("Enter desired Genre: ").title()
    dbCursor.execute(f"SELECT * FROM tblFilms WHERE Genre = '{genreValue}' ") 
    allRecords = dbCursor.fetchall()

    for eachRecord in allRecords:
        print(eachRecord)

def search_year():
    yearValue = input("Enter desired Year: ") 
    dbCursor.execute(f"SELECT * FROM tblFilms WHERE yearReleased = '{yearValue}' ") 
    allRecords = dbCursor.fetchall()

    for eachRecord in allRecords:
        print(eachRecord)

def search_rating():
    ratingValue = input("Enter desired Rating: ").upper() 
    dbCursor.execute(f"SELECT * FROM tblFilms WHERE Rating = '{ratingValue}' ") 
    allRecords = dbCursor.fetchall()

    for eachRecord in allRecords:
        print(eachRecord)   

if __name__ == "__main__":
    reports()
    search_genre()
    search_year()
    search_rating()

