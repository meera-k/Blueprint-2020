from pymongo import MongoClient
from flask import Flask, render_template, request, session
import datetime

app = Flask(__name__)
client = MongoClient("mongodb+srv://admin:admin@cluster0-e5pzb.mongodb.net/test?retryWrites=true&w=majority")
db = client['Blueprint-2020'] #database - only one necessary
zodiac_key = db['zodiac_key'] #collection - perfect zodiac key
data = db['data'] #collection - actual user data - will hold single and total session data
page_num = 0

@app.route('/', methods=['GET']) #specifies path and which methods it will work w
def home():
    return render_template('welcomepage.html', messages=messages.find({}), loggedIn = ('username' in session), username = session.get('username', '')) #returns html file sent to browser given the file and parameter for variables
    #find returns all elements that fit a certain condition (eg. 'ts': [certain date] )
