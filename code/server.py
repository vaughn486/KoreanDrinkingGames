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

# display quiz question #
@app.route('/quiz/<int:quiz_id>')
def pageview(quiz_id):
    if quiz_id > 5:
        return "Question not found", 404
    else:
        # object = data[restaurant_id-1]   # -1 to compensate for indexing starting at 0
        # edit_link = "/edit/" + str(quiz_id)
        return render_template('quiz.html')


@app.route('/quizresult')
def quizresult():
   return render_template('quizresult.html')   



# FUNCTIONS



# RUN
if __name__ == '__main__':
   app.run(debug = True)
   
