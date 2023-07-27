from flask import Flask, render_template, url_for


app = Flask(__name__, static_folder="statics", template_folder="templates")


@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
