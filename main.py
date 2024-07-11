
from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_url_path="/assets")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/assets/<filename>")
def assets(filename):
    return send_from_directory("assets", filename)

if __name__ == "__main__":
    app.run()
