from flask import Flask, render_template
from dotenv import load_dotenv
from flask import request

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

    columns = ["Film ID", "Title", "Year Released", "Rating", "Duration", "Genre"]
    return render_template("films.html", films=films, columns=columns)


@app.route("/add_film", methods=["GET", "POST"])
def add_film():
    from FilmFlix_db import Filmflix_db

    if request.method == "POST":
        title = request.form.get("title")
        year = request.form.get("year")
        if not (year.isdigit() and len(year) == 4):
            return render_template(
                "addfilm.html", error="Year must be a 4-digit number"
            )
        rating = request.form.get("rating")
        duration = request.form.get("duration")
        genre = request.form.get("genre")

        if not all([title, year, rating, duration, genre]):
            return render_template("addfilm.html", error="All fields required")

        db = Filmflix_db()
        db.add_film(title, year, rating, duration, genre)
        db.close()
        return render_template("addfilm.html", success=True)

    return render_template("addfilm.html")


@app.route("/delete_film", methods=["GET", "POST"])
def delete_film():
    from FilmFlix_db import Filmflix_db

    db = Filmflix_db()
    films = db.get_all_films()

    if request.method == "POST":
        film_id_str = request.form.get("filmID")

        if not film_id_str or not film_id_str.isdigit():
            db.close()
            return render_template(
                "deletefilm.html", error="Please select a film", films=films
            )

        film_id = int(film_id_str)

        if not db.film_exists(film_id):
            db.close()
            return render_template(
                "deletefilm.html", error="No film with that ID found", films=films
            )

        db.delete_film(film_id)
        db.close()
        return render_template("deletefilm.html", success=True, films=films)

    db.close()
    return render_template("deletefilm.html", films=films)


@app.route("/amend_film")
def amend_film():
    return "<h2>Amend Film TODO</h2>"


@app.route("/display_films_by_x")
def display_films_by_x():
    return "<h2>Display Films by X TODO</h2>"


if __name__ == "__main__":
    load_dotenv()
    app.run(debug=True)
