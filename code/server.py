from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from flask import Markup
app = Flask(__name__)

import re

# DATA

#question bank
#q will be the question
#media will be any necessary media
#a will be the bank of possible answers
#a_correct will be the index of the correct answer
#TO DO: 1) should id and a_correct be strings or ints? 2) add in real q and a
question = [
   {
      "id": "1",
      "q": "asghjoieajsgd",
      "media": "",
      "a": ["weretygh", "yrterds", "wretry"],
      "a_correct": 1
   },
   {
      "id": "2",
      "q": "wgrhifp;ovleas",
      "media": "",
      "a": ["ytre", "waretyu", "iujhygrfed"],
      "a_correct": 3
   },
   {
      "id": "3",
      "q": "qwaresty",
      "media": "",
      "a": ["wearestryfy", "ikujyhtg", "ujyh5tg4r"],
      "a_correct": 2
   },
   {
      "id": "4",
      "q": "rethgjh",
      "media": "",
      "a": ["retyuy", "kujhygtf", "arestdyf"],
      "a_correct": 1
   }
]

#user's quiz selections stored here
#a is their selection
user_quiz_data = [
   {
      "id": "1",
      "a": ""
   },
   {
      "id": "2",
      "a": ""
   },
   {
      "id": "3",
      "a": ""
   },
   {
      "id": "4",
      "a": ""
   }
]

num_of_questions = 4




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
    if quiz_id > num_of_questions:
        return "Question not found", 404
    else:
        object = question[quiz_id-1]   # -1 to compensate for indexing starting at 0
        quiz_id = quiz_id+1
        next_link = "/quiz/" + str(quiz_id) #link to next quiz question
        return render_template('quiz.html', object=object, user_quiz_data=user_quiz_data, next_link=next_link)


@app.route('/quizresult')
def quizresult():
   return render_template('quizresult.html')   



# FUNCTIONS



# RUN
if __name__ == '__main__':
   app.run(debug = True)
   
