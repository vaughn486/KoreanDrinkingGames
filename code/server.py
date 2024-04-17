from flask import Flask, redirect
from flask import render_template
from flask import Response, request, jsonify
from flask import Markup
from datetime import datetime  # Import the datetime module
app = Flask(__name__)

import re
from datetime import datetime

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
      "q": "Question 1",
      "media": "",
      "a": ["Correct", "Incorrect"],
      "a_correct": 0
   },
   {
      "id": "2",
      "q": "Question 2",
      "media": "",
      "a": ["Correct", "Incorrect"],
      "a_correct": 0
   },
   {
      "id": "3",
      "q": "Question 3",
      "media": "",
      "a": ["Correct", "Incorrect"],
      "a_correct": 0
   },
   {
      "id": "4",
      "q": "Question 4",
      "media": "",
      "a": ["Correct", "Incorrect"],
      "a_correct": 0
   }
]

current_quiz_question = 0
correct_answers_count = 0

#user's quiz selections stored here
user_quiz_data = [
   
]


content_culture = [
   {
      'id': 1,
      'title': 'Korean Drinking Culture - Korean Drinks',
      'last_accessed': None
      
   },
   {
      'id': 2,
      'title': 'Korean Drinking Culture - Cheers + General Drinking Etiquette',
      'last_accessed': None
   },
   {
      'id': 3,
      'title': 'Korean Drinking Culture - How to "cha"',
      'last_accessed': None
   }
]

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
page_entry_times = {}

# ROUTES

@app.route('/')
def homepage():
   return render_template('home.html')   

@app.route('/api/learn_culture/<int:lesson>')
def api_learn_culture(lesson):
    if 1 <= lesson <= len(content_culture):
        lesson_data = content_culture[lesson - 1]  # Fetch the lesson data
        return jsonify(lesson_data)  # Return data as JSON
    else:
        return jsonify({'error': 'Lesson not found'}), 404

# Route to handle the POST request and update last accessed time
@app.route('/api/update_last_accessed_culture', methods=['POST'])
def update_last_accessed_culture():
    lesson_id = request.form.get('lesson_id')
    lesson_id = int(lesson_id)
    # Find the lesson with the given ID and update the last accessed time
    for lesson in content_culture:
        if lesson['id'] == lesson_id:
            lesson['last_accessed'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return jsonify({'success': True})
    # If the lesson ID is not found
    return jsonify({'error': 'Lesson ID not found'}), 404

@app.route('/learn_culture/<int:lesson>')
def learn_culture(lesson):
   print("Content being passed:", content_culture[lesson - 1])
   return render_template('learn_culture.html', lesson=content_culture[lesson-1]) 

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
        lesson_data = content_games[lesson - 1]  
        return jsonify(lesson_data)
    else:
        return jsonify({'error': 'Lesson not found'}), 404
    
@app.route('/learn_games/<int:lesson>')
def learn_games(lesson):
    print("Content being passed:", content_games[lesson - 1])
    return render_template('learn_games.html', lesson=content_games[lesson-1]) 

@app.route('/enter_page/<page_name>', methods=['GET'])
def enter_page(page_name):
    # Record the current time as the last entry time for the page
    page_entry_times[page_name] = datetime.now().isoformat()
    print(page_entry_times)
    # Return a response with the entry time
    return jsonify({
        'page_name': page_name,
        'last_entry_time': page_entry_times[page_name]
    })


@app.route('/quiz')
def quiz():
   return render_template('quiz.html')

# data for quiz pages is sent here
@app.route('/quiz_data/<int:quiz_id>')
def quiz_data(quiz_id):
   global current_quiz_question
   if 1 <= quiz_id <= len(question):
      question_data = question[quiz_id-1]
      current_quiz_question = quiz_id  
      return jsonify(question_data)
   else:
      return jsonify({'Error': 'Question not found'}), 404

# returns current quiz question
@app.route('/get_current_question')
def get_current_id():
    global current_quiz_question
    return jsonify({'current_quiz_question': current_quiz_question})

# display quiz question #
@app.route('/quiz/<int:quiz_id>', methods=['GET', 'POST'])
def pageview(quiz_id):
    global current_quiz_question, correct_answers_count
    if quiz_id == 1:
        correct_answers_count = 0 
   
    current_quiz_question = quiz_id
    
    if quiz_id > len(question):
      return redirect('/quizresult')
    question_data = question[quiz_id - 1]
    print("get", quiz_id)

    if request.method == 'POST':
        selected_answer = request.form['answer']
        if selected_answer == question_data['a'][question_data['a_correct']]:
            correct_answers_count += 1
            print(quiz_id, correct_answers_count)
        
        if quiz_id > len(question):
            return redirect('/quizresult')
        else:
            return redirect(f'/quiz/{quiz_id+1}')
    return render_template('quiz.html', object=question_data, next_link=f'/quiz/{quiz_id + 1}', enumerate=enumerate)


@app.route('/quizresult')
def quizresult():
   return render_template('quizresult.html', correct_answers = correct_answers_count, total_questions=len(question))   



# FUNCTIONS



# RUN
if __name__ == '__main__':
   app.run(debug = True)
   
