from connect import *

def update_record():
    idField = input("Enter the Film ID requiring update: ")

    fieldName = input("Enter one of the following: title, yearReleased, rating, duration or genre: ")

    fieldValue = input(f"Enter the value for {fieldName}: ").title()

    fieldValue = "'"+fieldValue+"'"
    print(fieldValue)

    dbCursor.execute(f"UPDATE tblFilms SET {fieldName} = {fieldValue} WHERE FilmID = {idField}")

    dbCon.commit()
    print(f"Record {idField} updated in the tblFilms table. ")

if __name__ == "__main__":
    update_record()

