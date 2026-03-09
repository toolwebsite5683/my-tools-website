from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/password")
def password():
    return render_template("password.html")

@app.route("/wordcounter")
def wordcounter():
    return render_template("wordcounter.html")

@app.route("/random")
def random():
    return render_template("random.html")

@app.route("/age")
def age():
    return render_template("age.html")

@app.route("/case")
def case():
    return render_template("case.html")

@app.route("/calculator")
def calculator():
    return render_template("calculator.html")

@app.route("/qr")
def qr():
    return render_template("qr.html")

@app.route("/unit")
def unit():
    return render_template("unit.html")

@app.route("/username")
def username():
    return render_template("username.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

import random
import string
from flask import request

@app.route("/password", methods=["GET","POST"])
def password():

    password=""

    if request.method == "POST":
        
        length = int(request.form["length"])

        characters = string.ascii_letters + string.digits

        password ="".join(random.choice(characters) for i in range(length))

        return render_template("password.html", password=password)
