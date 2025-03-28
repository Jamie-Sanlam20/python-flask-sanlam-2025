from flask import Blueprint, render_template

HTTP_NOT_FOUND = 404
main_bp = Blueprint("main_bp", __name__)

# Pattern for creating new API
# / represents path


# API / Endpoint
@main_bp.get("/")
def hello_world():
    return "<h1>Super, Cool 😁</h1>"


name = "Jamie"
hobbies = ["Gaming", "Reading", "Soccer", "Ballet", "Gyming", "Yoga"]

# Flask uses Jinja2 -> looks for name in HTML and replaces {{}} with python value


@main_bp.get("/about")
def about_page():
    return render_template(
        "about.html", name=name, hobbies=hobbies
    )  # by default, flask will look at templates folder


# we want to make HTML more dynamic (changes Sanlam -> someone's name)
# name = name -> treated as keyword argument


profiles = [
    {
        "profile_pic": "https://static.vecteezy.com/system/resources/previews/001/131/187/large_2x/serious-man-portrait-real-people-high-definition-grey-background-photo.jpg",
        "name": "Adam",
    },
    {
        "profile_pic": "https://i.pinimg.com/originals/d3/4c/0a/d34c0aaa0e2cce6d2a0b47b641ff28af.jpg",
        "name": "Rose",
    },
    {
        "profile_pic": "https://c.stocksy.com/a/i8J500/z9/1265216.jpg",
        "name": "Caedon",
    },
]


@main_bp.get("/profile")
def profile_page():
    return render_template("profile.html", profiles=profiles)
