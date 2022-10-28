import sqlite3

connection = sqlite3.connect(r"C:\Users\david\OneDrive\Desktop\Network.py\unit2\2.6.3\user_questions.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE questions(
        question TEXT,
        options TEXT,
        right_answer TEXT
    )
""")

connection.commit()
connection.close()