from pymongo import MongoClient
from flask import Flask, render_template, request, session
from datetime import datetime

app = Flask(__name__)
client = MongoClient("mongodb+srv://admin:admin@cluster0-e5pzb.mongodb.net/test?retryWrites=true&w=jority")
db = client['Blueprint-2020'] #database - only one necessary
total_data = db['total_data'] #collection - actual user data - will hold single and total session data
single_data = []
signs_array = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

@app.route('/', methods=['GET']) #specifies path and which methods it will work w
def home(): 
    return render_template('questions.html') #returns html file sent to browser given the file and parameter for variables

# @app.route('/stats', methods=['GET'])
# def stats():
#     #add info to all_data doc in data collection
#     #do calculations
#     #clear out current user doc

@app.route('/submit', methods=['POST'])
def submit():
    raw_single = request.form['raw_single']
    for x in range(0, raw_single.length):
        if raw_single[x] == "Aries":
            single_data[0]+=1
        elif raw_single[x] == "Taurus":
            single_data[1]+=1
        elif raw_single[x] == "Gemini":
            single_data[2]+=1
        elif raw_single[x] == "Cancer":
            single_data[3]+=1
        elif raw_single[x] == "Leo":
            single_data[4]+=1
        elif raw_single[x] == "Virgo":
            single_data[5]+=1
        elif raw_single[x] == "Libra":
            single_data[6]+=1
        elif raw_single[x] == "Scorpio":
            single_data[7]+=1   
        elif raw_single[x] == "Sagittarius":
            single_data[8]+=1
        elif raw_single[x] == "Capricorn":
            single_data[9]+=1
        elif raw_single[x] == "Aquarius":
            single_data[10]+=1
        elif raw_single[x] == "Pisces":
            single_data[11]+=1
    max = 0
    for x in range (0, len(single_data)):
        if single_data[x] > max:
            max = single_data[x]
    sign = signs_array[x]
    matches = true
    if sign != single_data[12]:
        matches = false
        total_data[0]+=1
    total_data[1]+=1
    percent_wrong = total_data[0]/total_data[1]
    return render_template('results.html', matches=matches, predicted_sign=sign, actual_sign=single_data[12], percent_wrong=percent_wrong)

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

    #add info to all_data doc in data collection
    #do calculations
    #clear out current user doc

app.run(port=3000, debug=True)