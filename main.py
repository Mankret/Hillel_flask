from flask import Flask, request
from faker import Faker
import csv
from statistics import mean
import requests

app = Flask(__name__)
fake = Faker()


@app.route("/requirements/")
def requirement_return():
    with open('requirements.txt', 'r') as f:
        text = f.read()
        return text


@app.route('/generate-users/', methods=['GET'])
def get_generate_users():
    result_list = []
    query = request.args.get('count')
    for index in range(1, (int(query) + 1)):
        result_list.append(f'{index},  {fake.name()}, {fake.email()}')
    return result_list


@app.route('/mean/')
def upload_from_csv():
    with open("hw.csv", newline='') as f:
        reader = csv.DictReader(f)
        temp_dict = {}
        height_lst = []
        weight_lst = []
        for row in reader:
            temp_dict.update({'Height': row[' "Height(Inches)"'], 'Weight': row[' "Weight(Pounds)"']})
            height_lst.append(float(temp_dict['Height']))
            weight_lst.append(float(temp_dict['Weight']))
        mean_height = mean(height_lst) * 2.54
        mean_weight = mean(weight_lst) / 2.2505
        result = f' Средний рост: {mean_height.__round__()} см., Средний вес: {mean_weight.__round__()} кг.'
    return result


@app.route('/space/')
def space():
    r = requests.get("http://api.open-notify.org/astros.json")
    data = r.json()
    return f"Сейчас в космосе {data['number']} человек"


if __name__ == "__main__":
    app.run(debug=True)
