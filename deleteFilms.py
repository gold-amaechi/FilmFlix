from connect import *

def delete_record():
    idField = input("Enter Film ID to be deleted: ")

    dbCursor.execute(f"DELETE FROM tblFilms WHERE FilmID = {idField}")

    dbCon.commit()
    print(f"Record {idField} deleted")

if __name__ == "__main__":
    delete_record()