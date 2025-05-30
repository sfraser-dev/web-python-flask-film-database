import sqlite3
import os


# Handles DB operations for FilmFlix
class FilmflixModel:
    def __init__(self):
        base_dir = os.path.abspath(os.path.dirname(__file__))
        db_path = os.path.join(base_dir, "filmflix.db")
        self.con = sqlite3.connect(db_path)
        self.cursor = self.con.cursor()

    def get_all_films(self):
        sql = "SELECT * FROM films"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.con.close()

    def add_film(self, title, year, rating, duration, genre):
        # parameterised query to prevent SQL injection ("?" placeholders)
        sql = "INSERT INTO films (title, year, rating, duration, genre) VALUES (?, ?, ?, ?, ?)"
        values = (title, year, rating, duration, genre)
        self.cursor.execute(sql, values)
        self.con.commit()

    def film_exists(self, film_id):
        sql = "SELECT 1 FROM films WHERE id = ?"
        self.cursor.execute(sql, (film_id,))
        return self.cursor.fetchone() is not None

    def delete_film(self, film_id):
        sql = "DELETE FROM films WHERE id = ?"
        self.cursor.execute(sql, (film_id,))
        self.con.commit()

    def update_film_field(self, film_id, column_name, new_value):
        allowed_fields = ["title", "year", "rating", "duration", "genre"]
        if column_name not in allowed_fields:
            raise ValueError("Invalid column name")

        sql = f"UPDATE films SET {column_name} = ? WHERE id = ?"
        self.cursor.execute(sql, (new_value, film_id))
        self.con.commit()

    def get_films_by_title(self, title):
        sql = "SELECT * FROM films WHERE title LIKE ?"
        self.cursor.execute(sql, ("%" + title + "%",))
        return self.cursor.fetchall()

    def get_films_by_year(self, year):
        sql = "SELECT * FROM films WHERE year = ?"
        self.cursor.execute(sql, (year,))
        return self.cursor.fetchall()

    def get_films_by_rating(self, rating):
        sql = "SELECT * FROM films WHERE rating = ?"
        self.cursor.execute(sql, (rating,))
        return self.cursor.fetchall()

    def get_films_by_duration(self, duration):
        sql = "SELECT * FROM films WHERE duration = ?"
        self.cursor.execute(sql, (duration,))
        return self.cursor.fetchall()

    def get_films_by_genre(self, genre):
        sql = "SELECT * FROM films WHERE genre = ?"
        self.cursor.execute(sql, (genre,))
        return self.cursor.fetchall()
