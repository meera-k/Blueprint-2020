from pymongo import MongoClient
from flask import Flask, render_template, request, session
from datetime import datetime

app = Flask(__name__)
client = MongoClient("mongodb+srv://admin:admin@cluster0-e5pzb.mongodb.net/test?retryWrites=true&w=majority")
db = client['Blueprint-2020'] #database - only one necessary
zodiac_key = db['zodiac_key'] #collection - perfect zodiac key
data = db['data'] #collection - actual user data - will hold single and total session data
page_num = 0
question_dict = {1: "", 2: "", 3: ""}
answer_dict = {1: ["smart", "dumb"], 2: ["smart", "dumb"], 3: ["smart", "dumb"]}

@app.route('/', methods=['GET']) #specifies path and which methods it will work w
def welcome_page():
    return render_template('welcomepage.html') #returns html file sent to browser given the file and parameter for variables

@app.route('/next', methods=['GET', 'POST'])
def next():
    page_num += 1
    return render_template('questionpage.html', question=question_dict[page_num], answers=answer_dict[page_num])

@app.route('/birthday', methods=['POST'])
def birthday():
    render_template('birthdaypage.html')
    birthday = datetime.strptime(request.form['date'], '%m/%d/%y')
    if birthday < datetime(2020, 1, 20) or datetime(2020, 12, 23) < birthday:
        data['zodiac'] = 'Capricorn'
    elif datetime(2020, 1, 21) < birthday < datetime(2020, 2, 19):
        data['zodiac'] = 'Aquarius'
    elif datetime(2020, 2, 20) < birthday < datetime(2020, 3, 20):
        data['zodiac'] = 'Pisces'
    elif datetime(2020, 3, 21) < birthday < datetime(2020, 4, 20):
        data['zodiac'] = 'Aries'
    elif datetime(2020, 4, 21) < birthday < datetime(2020, 5, 21):
        data['zodiac'] = 'Taurus'
    elif datetime(2020, 5, 22) < birthday < datetime(2020, 6, 21):
        data['zodiac'] = 'Gemini'
    elif datetime(2020, 6, 22) < birthday < datetime(2020, 7, 22):
        data['zodiac'] = 'Cancer'
    elif datetime(2020, 7, 23) < birthday < datetime(2020, 8, 21):
        data['zodiac'] = 'Leo'
    elif datetime(2020, 8, 22) < birthday < datetime(2020, 9, 23):
        data['zodiac'] = 'Virgo'
    elif datetime(2020, 9, 24) < birthday < datetime(2020, 10, 23):
        data['zodiac'] = 'Libra'
    elif datetime(2020, 10, 24) < birthday < datetime(2020, 11, 22):
        data['zodiac'] = 'Scorpio'
    else: #if datetime(2020, 11, 23) < birthday < datetime(2020, 12, 22)
        data['zodiac'] = 'Sagittarius'
    return 'success'
    #TODO make sure that info is passed in in datetime format
    #add zodiac into cur_user doc as last entry

@app.route('/stats', methods=['GET'])
def stats():
    return 'f'
    #add info to all_data doc in data collection
    #do calculations
    #clear out current user doc