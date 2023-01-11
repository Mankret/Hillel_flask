from flask import (
    Blueprint, g, render_template, request, session
)
import csv
from statistics import mean
import requests
from .db import get_db
from faker import Faker
import sqlite3

fake = Faker()

bp = Blueprint('implement', __name__)


@bp.route("/")
def index():
    return render_template('base.html')


@bp.route("/requirements/")
def requirement_return():
    with open('requirements.txt', 'r') as f:
        text = f.read()
        return text


@bp.route('/generate-users/', methods=['GET'])
def get_generate_users():
    result_list = []
    query = request.args.get('count')
    for index in range(1, (int(query) + 1)):
        result_list.append(f'{index},  {fake.name()}, {fake.email()}')
    return result_list


@bp.route('/mean/')
def upload_from_csv():
    with open("./hw.csv", newline='') as f:
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


@bp.route('/space/')
def space():
    r = requests.get("http://api.open-notify.org/astros.json")
    data = r.json()
    return f"Сейчас в космосе {data['number']} человек"


@bp.route('/names/')
def names():
    db = get_db()
    cur = db.execute('''SELECT COUNT(DISTINCT(artist)) FROM tracks
                        ORDER by artist''')
    temp = cur.fetchall()
    artists = [x[0] for x in temp]
    return render_template('names.html', artists=artists)


@bp.route('/tracks/')
def tracks():
    total_count = session.get('tracks')
    numbers = get_db().execute('''SELECT COUNT (*) FROM tracks''').fetchone()
    return render_template('numbers.html', numbers=numbers)


@bp.route('/tracks/<genre>')
def tracks_genre(genre):
    db = get_db()
    cur = db.execute(f'''SELECT COUNT(genre) FROM tracks
                            WHERE genre = "{genre}"''')
    value = cur.fetchone()
    return render_template('genre.html', value=value)


@bp.route('/tracks-sec/')
def tracks_sec():
    db = get_db()
    cur = db.execute('''SELECT title, length FROM tracks''')
    length = cur.fetchall()
    return render_template('length_tracks.html', length=length)


@bp.route('/tracks-sec/statistics/')
def tracks_statistic():
    db = get_db()
    cur = db.execute('''SELECT ROUND(AVG(length)), SUM(length) FROM tracks''')
    length = cur.fetchall()
    return render_template('tracks_statistic.html', length=length)
