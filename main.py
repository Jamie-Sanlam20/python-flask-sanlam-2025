from flask import Flask, render_template

app = Flask(__name__)

# Pattern for creating new API
# / represents path


# API / Endpoint
@app.get("/")
def hello_world():
    return "<h1>Super, Cool 😁</h1>"


name = "Jamie"
hobbies = ["Gaming", "Reading", "Soccer", "Ballet", "Gyming", "Yoga"]

# Flask uses Jinja2 -> looks for name in HTML and replaces {{}} with python value


@app.get("/about")
def about_page():
    return render_template(
        "about.html", name=name, hobbies=hobbies
    )  # by default, flask will look at templates folder


# we want to make HTML more dynamic (changes Sanlam -> someone's name)
# name = name -> treated as keyword argument

# Flask - Blueprints
# connect movies_bp.py and main (postman only reads main file)

# connection:
from routes.movies_bp import movies_bp  # folder name + file name

app.register_blueprint(
    movies_bp, url_prefix="/movies"
)  # don't have to repeat in methods url
# prefix -> Refactor -> maintainability ⬆️ (change in one place)

if __name__ == "__main__":
    app.run(debug=True)

# to re-stablish connection: Ctrl + C -> closes connection
# flask --app main run
# if you switch Debug on, it will automatically save (restart app)

# python .\main.py -> restart flask connection

# Ctrl + ~ -> Open + Close terminal
