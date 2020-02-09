from pymongo import MongoClient
from flask import Flask, render_template, request, session
from datetime import datetime

app = Flask(__name__)
client = MongoClient("mongodb+srv://admin:admin@cluster0-e5pzb.mongodb.net/test?retryWrites=true&w=jority")
db = client['Blueprint-2020'] #database - only one necessary
total_data = db['total_data'] #collection - actual user data - will hold single and total session data
single_data = []

@app.route('/', methods=['GET']) #specifies path and which methods it will work w
def home():
    return render_template('questions.html') #returns html file sent to browser given the file and parameter for variables

# @app.route('/stats', methods=['GET'])
# def stats():
#     #add info to all_data doc in data collection
#     #do calculations
#     #clear out current user doc

@app.route('/birthday', methods=['POST'])
def birthday():
    birthday = datetime.strptime(request.form['date'], '%m/%d/%y') #TODO month and day
    if birthday < datetime(2020, 1, 20) or datetime(2020, 12, 23) < birthday:
        single_data.append('Capricorn')
    elif datetime(2020, 1, 21) < birthday < datetime(2020, 2, 19):
        single_data.append('Aquarius')
    elif datetime(2020, 2, 20) < birthday < datetime(2020, 3, 20):
        single_data.append('Pisces')
    elif datetime(2020, 3, 21) < birthday < datetime(2020, 4, 20):
        single_data.append('Aries')
    elif datetime(2020, 4, 21) < birthday < datetime(2020, 5, 21):
        single_data.append('Taurus')
    elif datetime(2020, 5, 22) < birthday < datetime(2020, 6, 21):
        single_data.append('Gemini')
    elif datetime(2020, 6, 22) < birthday < datetime(2020, 7, 22):
        single_data.append('Cancer')
    elif datetime(2020, 7, 23) < birthday < datetime(2020, 8, 21):
        single_data.append('Leo')
    elif datetime(2020, 8, 22) < birthday < datetime(2020, 9, 23):
        single_data.append('Virgo')
    elif datetime(2020, 9, 24) < birthday < datetime(2020, 10, 23):
        single_data.append('Libra')
    elif datetime(2020, 10, 24) < birthday < datetime(2020, 11, 22):
        single_data.append('Scorpio')
    else: #if datetime(2020, 11, 23) < birthday < datetime(2020, 12, 22)
        single_data.append('Sagittarius')
    return 'success'

@app.route('/stats', methods=['GET'])
def stats():

    return 'f'
    #add info to all_data doc in data collection
    #do calculations
    #clear out current user doc

app.run(port=3000, debug=True)