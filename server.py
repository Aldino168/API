from flask import Flask, Response, request
import pymongo
import json
from bson.objectid import ObjectId

import pandas as pd
import pickle
import os


import ocr
from PIL import Image
import torch
import easyocr
import re

app=Flask(__name__)
#######################################
try:
    mongo = pymongo.MongoClient(
        host= "localhost",
        port = 27017,
        serverSelectionTimeoutMS =1000
    )
    db = mongo.final
    mongo.server_info()
except: 
    print("ERROR - Cannot connect to mongodb")
#######################################
@app.route('/users', methods=['POST'])
def create_user():
    try:
        csvfile = request.files["file"]
        img = Image.open(csvfile)
        img = img.save("data/images/zzzz.jpg")
        konek = ocr.connect()
        semua = ocr.diskon1(konek)
        user = {
            "disc" : semua[0],
            "hargadisc" : semua[1],
            "harga" : semua[2],
            "produk" : semua[3]
        }
        dbResponse = db.users.insert_one(user)
        # print(dbResponse.inserted_id)

        return Response(
            response= json.dumps(
                {
                    "massage": "user created",
                    "id": f"{dbResponse.inserted_id}"
                }
            ), status = 200,
            mimetype = "application/json"
        )

    except Exception as e:
        print(e)
#######################################
@app.route('/users', methods=["GET"])
def read_user():
    try:
        data = list(db.users.find())
        for user in data:
            user["_id"] = str(user['_id'])
        return Response(
            response= json.dumps(data),
            status=500,
            mimetype="application/json"
        )
    except Exception as e:
        print(e)
        return Response(
            response= json.dumps(
                {"massage": "cannot read users"})
                , status = 500,
                mimetype = "application/json"
        )


#######################################


if __name__ == "__main__":
    app.run(port=80, debug=True)