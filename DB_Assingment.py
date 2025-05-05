import sqlite3
import re

#List of files
fileList = ('information.docs','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
#connect to sql database
conn = sqlite3.connect('file_database.db')

#creates a table if it doesnt already exist
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS file_list( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        file_name TEXT)")

#finds what files are .txt files
    for file_name in fileList:
        if re.search(r'\.txt$', file_name):
            cur.execute("INSERT INTO file_list(file_name) VALUES (?)", (file_name,))
    conn.commit()

    cur.execute("SELECT file_name FROM file_list")
    text_files = cur.fetchall()
#prints what files are .txt files
    print("Text files: ")
    for text_file in text_files:
        print(text_file[0])
conn.close()






