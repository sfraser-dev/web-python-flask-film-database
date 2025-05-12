import sqlite3
import os

# Handles DB operations for FilmFlix
class Filmflix_db:
    def __init__(self):
        base_dir = os.path.abspath(os.path.dirname(__file__))
        db_path = os.path.join(base_dir, 'filmflix.db')
        self.con = sqlite3.connect(db_path)
        self.cursor = self.con.cursor()

    def get_all_films(self):
        sql = "SELECT * FROM films"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.con.close()