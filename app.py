from flask import Flask, render_template, request
from werkzeug import secure_filename
import os
import sys
from PIL import Image
import pytesseract
import argparse

# import cv2

__author__ = "Rick Torzynski <ricktorzynski@gmail.com>"
__source__ = ""

app = Flask(__name__)
UPLOAD_FOLDER = "./static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/uploader", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        f = request.files["file"]

        # create a secure filename
        filename = secure_filename(f.filename)

        # save file to /static/uploads
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        f.save(filepath)
        text = pytesseract.image_to_string(Image.open(filepath))

        os.remove(filepath)

        return render_template("uploaded.html", displaytext=text, fname=filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

