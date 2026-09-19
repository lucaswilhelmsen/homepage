from flask import Flask, request, session, render_template, redirect
import os 

templates = os.path.dirname(__file__)

app = Flask(__name__)


@app.template_filter()
def add_linebreak(value):
    if value:
        return value.replace("\n", "<br>")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index")
def back_index():
    return render_template("index.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/writing")
def writing():
    return render_template("writing.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/pictures")
def pictures():
    return render_template("pictures.html")

if __name__ == "__main__":
    print("Starting Flask server on http://localhost:5000")
    app.run(debug=True, port=5000)