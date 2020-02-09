from pymongo import MongoClient
from flask import Flask, render_template, request, session
import datetime

app = Flask(__name__)
client = MongoClient("mongodb+srv://admin:admin@cluster0-e5pzb.mongodb.net/test?retryWrites=true&w=majority")
db = client['Blueprint-2020'] #database - only one necessary
zodiac_key = db['zodiac_key'] #collection - perfect zodiac key
data = db['data'] #collection - actual user data - will hold single and total session data
page_num = 0
question_dict = {1: "",2: "",3: ""}
answer_dict = {1: ["smart", "dumb"], 2: ["smart", "dumb"], 3: ["smart", "dumb"],}

@app.route('/', methods=['GET']) #specifies path and which methods it will work w
def welcome_page():
    return render_template('welcomepage.html') #returns html file sent to browser given the file and parameter for variables
    #find returns all elements that fit a certain condition (eg. 'ts': [certain date] )

@app.route('/next', methods=['GET', 'POST'])
def next():
    page_num++
    return render_template('questionpage.html', question_dict[page_num], answer_dict[page_num])

@app.route('/birthday', methods=['POST'])
def birthday():
    #TODO make sure that info is passed in in datetime format

@app.route('/stats', methods=['GET'])
def stats():
    #add info to all_data doc in data collection
    #do calculations
    #clear out current user doc