from flask import Flask, request, session, render_template, redirect
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os 

templates = os.path.dirname(__file__)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

print("Database URL:", app.config["SQLALCHEMY_DATABASE_URI"])

try:
    engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1")).fetchone()
        print("Database connection successful!")
except Exception as e:
    print("Database connection failed:", e)
    exit(1)

Session = sessionmaker(bind=engine)

@app.template_filter()
def add_linebreak(value):
    if value:
        return value.replace("\n", "<br>")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index")
def back_index():
    print("Back to main page route accessed")
    return render_template("index.html")

@app.route("/portfolio")
def portfolio():
    print("Portfolio route accessed")
    try:
        session = Session()
        result = session.execute(text('SELECT "image-address", "portfolio-item", "github-link", "readme" FROM portfolio')).fetchall()
        print("Portfolio data:", result)
        session.close()
        data_list = []
        for row in result:
            portfolio_dict = {
                "image-address": row[0],
                "portfolio-item": row[1],
                "github-link": row[2],
                "readme": row[3]
            }
            data_list.append(portfolio_dict)
        
        print(f"Rendering template with {len(data_list)} portfolio items")
        return render_template("portfolio.html", portfolio=data_list)
    except Exception as e:
        print(f"Error in portfolio route: {e}")
        return f"Error: {e}", 500



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

