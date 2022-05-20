import pandas as pd
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)
model=pickle.load(open("model/linear-weight.pkl","rb"))

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("portofolio2.html")
    elif request.method == "POST":
        csvfile = request.files.get("file")
        X_test = pd.read_csv(csvfile)
        X_test["pred"] = model.predict(X_test)
        return X_test.to_html()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")