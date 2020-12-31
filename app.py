import re
from statistics import mean
from itertools import count
import pymongo

from flask import Flask
from flask import render_template
from flask import url_for
from flask import request

app = Flask(__name__, static_folder='static')

client = pymongo.MongoClient('mongodb://st:askldjwq@185.93.109.237:27019/?authSource=goscatalog')
db = client.goscatalog
myc = db.things
cursor = list(myc.find())
collection = cursor


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('about.html', collection=collection)


@app.route('/list', methods=['GET', 'POST'])
def lst():
    return render_template('list.html', collection=collection)


@app.route('/object/<id>', methods=['GET', 'POST'])
def obj(id):
    data = ''
    for row in collection:
        if row['_id'] == id:
            data = row
            break
    desc = '-'
    museum = '-'
    period = '-'
    tech = '-'
    image = '-'
    if 'description' in data['data']:
        desc = data['data']['description']
    if 'museum' in data['data']:
        museum = data['data']['museum']['name']
    if 'periodStr' in data['data']:
        period = data['data']['periodStr']
    if 'technologies' in data['data']:
        tech = data['data']['technologies'][0]
    if 'images' in data['data']:
        image = data['data']['images'][0]['url']

    return render_template('object.html', id=id, data=data, desc=desc, museum=museum, period=period, tech=tech,
                           image=image)
