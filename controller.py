from flask import Flask, render_template
from dotenv import load_dotenv
from flask import request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/films")
def all_films():
    from model import FilmflixModel

    db = FilmflixModel()
    films = db.get_all_films()
    db.close()

    columns = ["Film ID", "Title", "Year Released", "Rating", "Duration", "Genre"]
    return render_template("films.html", films=films, columns=columns)


@app.route("/add_film", methods=["GET", "POST"])
def add_film():
    from model import FilmflixModel

    if request.method == "POST":
        title = request.form.get("title")
        year = request.form.get("year")
        if not (year.isdigit() and len(year) == 4):
            return render_template(
                "add_film.html", error="Year must be a 4-digit number"
            )
        rating = request.form.get("rating")
        duration = request.form.get("duration")
        genre = request.form.get("genre")

        if not all([title, year, rating, duration, genre]):
            return render_template("add_film.html", error="All fields required")

        db = FilmflixModel()
        db.add_film(title, year, rating, duration, genre)
        db.close()
        return render_template("add_film.html", success=True)

    return render_template("add_film.html")


@app.route("/delete_film", methods=["GET", "POST"])
def delete_film():
    from model import FilmflixModel

    db = FilmflixModel()
    films = db.get_all_films()

    if request.method == "POST":
        film_id_str = request.form.get("filmID")

        if not film_id_str or not film_id_str.isdigit():
            db.close()
            return render_template(
                "delete_film.html", error="Please select a film", films=films
            )

        film_id = int(film_id_str)

        if not db.film_exists(film_id):
            db.close()
            return render_template(
                "delete_film.html", error="No film with that ID found", films=films
            )

        db.delete_film(film_id)
        db.close()
        return render_template("delete_film.html", success=True, films=films)

    db.close()
    return render_template("delete_film.html", films=films)


@app.route("/amend_film", methods=["GET", "POST"])
def amend_film():
    from model import FilmflixModel

    db = FilmflixModel()
    films = db.get_all_films()
    db.close()

    if request.method == "POST":
        film_id_str = request.form.get("filmID")
        column = request.form.get("column")
        new_value = request.form.get("new_value")

        if not film_id_str or not film_id_str.isdigit():
            return render_template(
                "amend_film.html", films=films, error="Please select a valid film"
            )

        if column not in ["title", "year", "rating", "duration", "genre"]:
            return render_template(
                "amend_film.html", films=films, error="Invalid field selection"
            )

        if not new_value:
            return render_template(
                "amend_film.html", films=films, error="Please enter a new value"
            )

        film_id = int(film_id_str)
        db = FilmflixModel()
        if not db.film_exists(film_id):
            db.close()
            return render_template(
                "amend_film.html", films=films, error="Film not found"
            )

        db.update_film_field(film_id, column, new_value)
        db.close()
        return render_template("amend_film.html", films=films, success=True)

    return render_template("amend_film.html", films=films)


@app.route("/search", methods=["GET", "POST"])
def search():
    from model import FilmflixModel

    columns = ["Film ID", "Title", "Year Released", "Rating", "Duration", "Genre"]
    results = []

    if request.method == "POST":
        field = request.form.get("field")
        value = request.form.get("value")

        if not field or not value:
            return render_template(
                "reports.html",
                columns=columns,
                results=[],
                error="Both field and value required",
            )

        db = FilmflixModel()
        method_name = f"get_films_by_{field}"

        if hasattr(db, method_name):
            method = getattr(db, method_name)
            results = method(value)
        else:
            db.close()
            return render_template(
                "reports.html",
                columns=columns,
                results=[],
                error="Invalid field selected",
            )
        db.close()

        return render_template("reports.html", columns=columns, results=results)

    return render_template("reports.html", columns=columns, results=[])


if __name__ == "__main__":
    load_dotenv()
    app.run(debug=True)
