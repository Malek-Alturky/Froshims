from flask import Flask, render_template, request, redirect

app = Flask(__name__)

SPORTS = ["Basketball", "Football", "Boxing"]

REGISTRANTS = {}

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS )


@app.route("/register", methods=["POST"])

def register():
    # Validate the name
    name = request.form.get("name")
    if not name:
        return render_template("error.html", message="Mssing Name")

    # Validate the Sports
    sport = request.form.get("sport")

    if not sport:
        return render_template("error.html", message="Mssing Sport")

    if sport not in SPORTS:
        return render_template("error.html", message="Invalid Sport")

    # Fill the list 
    REGISTRANTS[name] = sport

    return redirect("/registrants")

@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=REGISTRANTS)