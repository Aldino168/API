import pandas as pd
import pickle
import os
from flask import Flask, render_template, request

import ocr
from PIL import Image
import torch
import easyocr
import re

app = Flask(__name__)


@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("portofolio2.html")
    elif request.method == "POST":
        csvfile = request.files.get("file")
        img = Image.open(csvfile)
        img = img.save("data/images/zzzz.jpg")
        konek = ocr.connect()
        semua = ocr.diskon1(konek)
        return print(semua)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")