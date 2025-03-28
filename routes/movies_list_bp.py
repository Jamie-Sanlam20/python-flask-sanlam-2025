from flask import Blueprint, render_template, request

from constants import STATUS_CODE
from extensions import db
from models.movie import Movie

HTTP_NOT_FOUND = 404
movies_list_bp = Blueprint("movies_list_bp", __name__)


@movies_list_bp.get("/")
def movie_list_page():
    movies = Movie.query.all()
    movies_dict = [movie.to_dict() for movie in movies]
    return render_template("movie-list.html", movies=movies_dict)
    # return render_template("movie-list.html", movies=movies)


@movies_list_bp.get("/<id>")
def movie_details(id):
    movie = Movie.query.get(id)

    if not movie:
        return {"message": "Movie not found"}, HTTP_NOT_FOUND  # returning a tuple

    data = movie.to_dict()
    return render_template("movie-details.html", movie=data)

    # for movie in movies:
    #     if movie["id"] == id:
    #         return render_template("movie-details.html", movie=movie)
    # return render_template("not-found.html")
