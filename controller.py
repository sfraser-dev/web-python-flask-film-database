from flask import Flask, render_template
from dotenv import load_dotenv

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/films")
def all_films():
    from FilmFlix_db import Filmflix_db

    db = Filmflix_db()
    films = db.get_all_films()
    db.close()

    columns = ['Film ID', 'Title', 'Year Released', 'Rating', 'Duration', 'Genre']
    return render_template("films.html", films=films, columns=columns)

@app.route("/add_film")
def add_film():
    return "<h2>Add Film TODO</h2>"


@app.route("/delete_film")
def delete_film():
    return "<h2>Delete Film TODO</h2>"


@app.route("/amend_film")
def amend_film():
    return "<h2>Amend Film TODO</h2>"


@app.route("/display_films_by_x")
def display_films_by_x():
    return "<h2>Display Films by X TODO</h2>"


if __name__ == "__main__":
    load_dotenv()
    app.run(debug=True)
