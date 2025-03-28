from flask import Flask, render_template
from sqlalchemy.sql import text

from config import Config
from extensions import db
from models.movie import Movie
from routes.main_bp import main_bp  # connection: folder name + file name
from routes.movies_bp import movies_bp
from routes.movies_list_bp import movies_list_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # dialling it in - establishing connection

    # Initialize the DB - calling DB
    db.init_app(app)

    with app.app_context():
        try:
            result = db.session.execute(
                text("SELECT 1")
            ).fetchall()  # testing connection
            # print(Movie.query.all())
            # movies = Movie.query.all()
            # print(movies[0].to_dict())
            print("Connection successful:", result)
        except Exception as e:
            print("Error connecting to the database:", e)

    # Flask - Blueprints
    # connect movies_bp.py and main (postman only reads main file)

    # don't have to repeat in methods url
    # prefix -> Refactor -> maintainability ⬆️ (change in one place)

    app.register_blueprint(main_bp)
    app.register_blueprint(movies_bp, url_prefix="/movies")
    app.register_blueprint(movies_list_bp, url_prefix="/movie-list")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

# to re-stablish connection: Ctrl + C -> closes connection
# flask --app main run
# if you switch Debug on, it will automatically save (restart app)

# python .\main.py -> restart flask connection

# Ctrl + ~ -> Open + Close terminal

# .\myenv\Scripts\Activate.ps1
