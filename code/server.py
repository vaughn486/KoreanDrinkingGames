from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from flask import Markup
app = Flask(__name__)

import re




# ROUTES

@app.route('/')
def homepage():
   return render_template('home.html')   

@app.route('/learn')
def learn():
   return render_template('learn.html')   

@app.route('/quiz')
def quiz():
   return render_template('quiz.html')   



# FUNCTIONS



# RUN
if __name__ == '__main__':
   app.run(debug = True)
   
