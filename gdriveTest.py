#import library
import gspread
#Service client credential from oauth2client
from oauth2client.service_account import ServiceAccountCredentials
# Print nicely
import pprint
import random
import git
import os

from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

#Create scope
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
#create some credential using that scope and content of startup_funding.json
creds = ServiceAccountCredentials.from_json_keyfile_name('GSD.json',scope)
#create gspread authorize using that credential
client = gspread.authorize(creds)
#Now will can access our google sheets we call client.open on StartupName
sheet = client.open('AppDictionary').sheet1
pp = pprint.PrettyPrinter()
#Access all of the record inside that
result = sheet.get_all_records()

currentWord=""

@app.route('/game')
def index2():
  sheet = client.open('AppDictionary').sheet1
  result1 = sheet.get_all_records()
  samples=random.sample(range(0, len(result1)-1), 5)
  resp=[]
  for i in range (0,5):
  	resp.append(result1[i])
  return {'data':resp}

@app.route('/pull')
def pull():
	g = git.cmd.Git(git_dir)
	g.pull()

@app.route('/alldata')
def index1():
  return {'data':result}

@app.route('/randomWord')
def index3():
	sheet = client.open('AppDictionary').sheet1
	result1 = sheet.get_all_records()
	return {'data':result1[random.randint(0,len(result1)-1)]}