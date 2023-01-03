from flask import Flask, request
from faker import Faker
import csv
from statistics import mean
import requests

app = Flask(__name__)
fake = Faker()


@app.route("/requirements/")
def requirement_return():
    return
    pass


@app.route('/generate-users/', methods=['GET'])
def get_generate_users():
    return
    pass


@app.route('/mean/')
def upload_from_csv():
    return
    pass


@app.route('/space/')
def space():
    return
    pass


if __name__ == "__main__":
    app.run(debug=True)
