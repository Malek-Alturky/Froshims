from flask import Flask, render_template, request

app = Flask(__name__)

SPORTS = ["Basketball", "Football", "Boxing"]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS )


@app.route("/register", methods=["POST"])

def register():
    # Validate the name
    name = request.form.get("name")
    if not name:
        return render_template("faliure.html")

    # Validate the Sports
    sports = request.form.getlist("sport")

    if not sports:
        return render_template("faliure.html")

    for sport in sports:
        if sport not in SPORTS:
            return render_template("faliure.html")

    return render_template("success.html")
