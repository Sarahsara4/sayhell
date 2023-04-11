from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "shahrukh"

@app.route("/hello")
def index():
    flash("What's your name?")
    return render_template ("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("hi " + str(request.form['mame_input']) + ", great to see you")
    return render_template ("index.html")