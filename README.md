<!-- markdownlint-disable MD007 -->
# Film Database Project (FilmFlix)

## MVC

This project is built using the Model-View-Controller (MVC) design pattern:

- Model:
    - `FilmFlix_db.py` handles all interactions with the SQLite database (queries, inserts, updates, deletes)
- View:
    - HTML templates in the templates/ folder (using Jinja2) display dynamic content in the browser
- Controller:
    - `controller.py` contains all the Flask routes that handle user input and control the flow of data between model and view

## Evolution

This web application builds upon an earlier command-line version of the FilmFlix database project. The CLI version interacted with the database through textual menus, while this version introduces a modern browser-based interface powered by Flask and W3.CSS.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
flask run
```
