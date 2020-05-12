import os
from flask import Flask, render_template
from app import app

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost/insta_scraper"
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/insta_scraper"
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = False

# app = Flask(__name__)
db = SQLAlchemy(app)

migrate = Migrate(app, db)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    return render_template("dashboard.html")

if __name__ == '__main__':
    app.run(debug=True)
