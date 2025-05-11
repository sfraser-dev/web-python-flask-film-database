from flask import Flask, render_template
from dotenv import load_dotenv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("base.html")  # Uses templates/base.html

if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True)
