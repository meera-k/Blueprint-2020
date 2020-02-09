from pymongo import MongoClient
from flask import Flask, render_template, request, session
import datetime

app = Flask(__name__)
client = MongoClient("mongodb+srv://admin:admin@cluster0-e5pzb.mongodb.net/test?retryWrites=true&w=majority")
db = client['Blueprint-2020'] #database - only one necessary
zodiac_key = db['zodiac_key'] #collection - perfect zodiac key
data = db['data'] #collection - actual user data - will hold single and total session data
