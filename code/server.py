from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from flask import Markup
from datetime import datetime  # Import the datetime module
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

content_etiquette = [
   {
      'id': 1,
      'title': 'Formal Drinking Etiquette - Summary',
      'last_accessed': None
      
   },
   {
      'id': 2,
      'title': 'Formal Drinking Etiquette - Rule 1',
      'last_accessed': None
   },
   {
      'id': 3,
      'title': 'Formal Drinking Etiquette - Rule 2',
      'last_accessed': None
   },
   {
      'id': 4,
      'title': 'Formal Drinking Etiquette - Rule 3',
      'last_accessed': None
   }
]

content_games = [
    {
        'id': 1,
        'title': 'Nunchi Game (눈치게임)',
        'description': 'Everyone begins shouting out numbers starting from 1 and going in order until the final person has said a number.'
    },
    {
        'id': 2,
        'title': 'Sam-Yuk-Gu (3-6-9) 삼–육–구',
        'description': 'At the beginning of each round, everyone chants Sam-Yuk-Gu 4x. Each player says one number counting up, going in a circle, but for each instance of a digit of 3, 6 or 9 you have to clap.'
    }
]


# ROUTES

@app.route('/')
def homepage():
   return render_template('home.html')   

@app.route('/learn_culture/<int:lesson>')
def learn_culture(lesson):
    return render_template('learn_culture.html', lesson=lesson) 

@app.route('/api/learn_etiquette/<int:lesson>')
def api_learn_etiquette(lesson):
    if 1 <= lesson <= len(content_etiquette):
        lesson_data = content_etiquette[lesson - 1]  # Fetch the lesson data
        return jsonify(lesson_data)  # Return data as JSON
    else:
        return jsonify({'error': 'Lesson not found'}), 404

# Route to handle the POST request and update last accessed time
@app.route('/api/update_last_accessed_etiquette', methods=['POST'])
def update_last_accessed_etiquette():
    lesson_id = request.form.get('lesson_id')
    lesson_id = int(lesson_id)
    # Find the lesson with the given ID and update the last accessed time
    for lesson in content_etiquette:
        if lesson['id'] == lesson_id:
            lesson['last_accessed'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return jsonify({'success': True})
    # If the lesson ID is not found
    return jsonify({'error': 'Lesson ID not found'}), 404

@app.route('/learn_etiquette/<int:lesson>')
def learn_etiquette(lesson):
   print("Content being passed:", content_etiquette[lesson - 1])
   return render_template('learn_etiquette.html', lesson=content_etiquette[lesson-1]) 

@app.route('/api/learn_games/<int:lesson>')
def api_learn_games(lesson):
    if 1 <= lesson <= len(content_games):
        lesson_data = content_games[lesson - 1]  # Fetch the lesson data
        return jsonify(lesson_data)  # Return data as JSON
    else:
        return jsonify({'error': 'Lesson not found'}), 404
    
@app.route('/learn_games/<int:lesson>')
def learn_games(lesson):
    print("Content being passed:", content_games[lesson - 1])
    return render_template('learn_games.html', lesson=content_games[lesson-1]) 


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
   
