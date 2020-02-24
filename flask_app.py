import task3
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


def before_request():
    app.jinja_env.cache = {}


app.before_request(before_request)


@app.route("/", methods=["GET", "POST"])
def index():
    print("INDEX")
    if request.method == "GET":
        print("GET")
        return render_template("main_page.html")

    if request.method == "POST":
        print("POST")
        task3.build_map(request.form['contents'])
        return redirect(url_for('map'))


@app.route("/map", methods=["GET"])
def map():
    return render_template("friends.html")

if __name__ == "__main__":
    app.run(debug = True)