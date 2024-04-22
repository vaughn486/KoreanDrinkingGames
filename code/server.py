from flask import Flask, redirect, url_for
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
      "q": "건배 (geonbae)",
      "media": "[media test]",
      "a": ["Cheers", "Soju + Beer Mix"],
      "a_correct": 0
   },
   {
      "id": "2",
      "q": "In the game Sam-Yuk-Gu, player 3 clapped once for the number 33:",
      "media": "",
      "a": ["Correct", "Drink!"],
      "a_correct": 1
   },
   {
      "id": "3",
      "q": "A man and his grandson are drinking soju. The grandson is feeling a bit woozy and says he’d like to stop drinking. Is this proper etiquette?",
      "media": "",
      "a": ["Correct Test", "Incorrect Test"],
      "a_correct": 0
   },
   {
      "id": "4",
      "q": "Sam says 1. Both Elaine and Grace say 2. Who drinks?",
      "media": "",
      "a": ["Elaine", "Elaine + Grace"],
      "a_correct": 1
   },
   {
      "id": "5",
      "q": "SoMaek has how many shots of soju?",
      "media": "",
      "a": ["1", "2"],
      "a_correct": 0
   },
   {
      "id": "6",
      "q": "In the game Sam-Yuk-Gu:",
      "media": "",
      "a": ["Correct Test", "Incorrect Test"],
      "a_correct": 0
   },
   {
      "id": "7",
      "q": "What is the proper way a new hire should pour a VP’s drink?",
      "media": "",
      "a": ["Correct Test", "Incorrect Test"],
      "a_correct": 0
   },
   {
      "id": "8",
      "q": "In the Nunchi Game:",
      "media": "",
      "a": ["Correct Test", "Incorrect Test"],
      "a_correct": 0
   }
]

correct_answers_count = 0

#user's quiz selections stored here
user_quiz_data = [
   
]


content = [
    {
        'id': 1,
        'name': 'Korean Drinking Culture',
        'explanation': 'Learn about different types of drinks, how to cheers, and how to "cha". ',
        'link': '/learn_culture/1'
    },
    {
        'id': 2,
        'name': 'Korean Drinking Etiquette',
        'explanation': 'Learn about basic Korean drinking etiquette, which includes how to pour and drink alcohol. ',
        'link': '/learn_etiquette/1'
    },
    {
        'id': 3,
        'name': 'Korean Drinking Games',
        'explanation': 'Learn about two popular Korean drinking games: Nunchi and Sam-Yuk-Gu.',
        'link': '/learn_games/1'
    }
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
   global correct_answers_count
   correct_answers_count = 0
   return render_template('home.html', current_page='home')   

@app.route('/api/learn_culture/<int:lesson>')
def api_learn_culture(lesson):
    global correct_answers_count
    correct_answers_count = 0
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
   global correct_answers_count
   correct_answers_count = 0
   print("Content being passed:", content_culture[lesson - 1])
   return render_template('learn_culture.html', lesson=content_culture[lesson-1], current_page='learning_culture') 

@app.route('/api/learn_etiquette/<int:lesson>')
def api_learn_etiquette(lesson):
    global correct_answers_count
    correct_answers_count = 0
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
   global correct_answers_count
   correct_answers_count = 0
   print("Content being passed:", content_etiquette[lesson - 1])
   return render_template('learn_etiquette.html', lesson=content_etiquette[lesson-1], current_page='learning_etiquette') 

@app.route('/api/learn_games/<int:lesson>')
def api_learn_games(lesson):
    global correct_answers_count
    correct_answers_count = 0
    if 1 <= lesson <= len(content_games):
        lesson_data = content_games[lesson - 1]  
        return jsonify(lesson_data)
    else:
        return jsonify({'error': 'Lesson not found'}), 404
    
@app.route('/learn_games/<int:lesson>')
def learn_games(lesson):
    global correct_answers_count
    correct_answers_count = 0
    print("Content being passed:", content_games[lesson - 1])
    return render_template('learn_games.html', lesson=content_games[lesson-1], current_page='learning_games') 

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
   global correct_answers_count
   correct_answers_count = 0
   return render_template('quiz_home.html', current_page='quiz')

# display quiz question #
@app.route('/quiz/<int:quiz_id>', methods=['GET', 'POST'])
def pageview(quiz_id):
   global correct_answers_count
   if quiz_id == 1:
      correct_answers_count = 0 
       
   if quiz_id > len(question):
      return redirect('/quizresult')
   
   question_data = question[quiz_id - 1]
   # print("get", quiz_id)

   # handles user's choice
   if request.method == 'POST':
      selected_answer = request.form['answer']
      if selected_answer == question_data['a'][question_data['a_correct']]:
         correct_answers_count += 1
         print(quiz_id, correct_answers_count)
        
      # handles reaching end of quiz / advancing to next question
      if quiz_id > len(question):
         return redirect('/quizresult')
      else:
         return redirect(f'/quiz/{quiz_id+1}')

   # renders current question 
   return render_template('quiz.html', object=question_data, enumerate=enumerate, current_page='quiz')


@app.route('/quizresult')
def quizresult():
   return render_template('quizresult.html', correct_answers = correct_answers_count, total_questions=len(question), current_page='quiz')   

@app.route('/learn_home/<int:id>')
def learn_home(id):
   # sending info to the learn home page
   object = content[id-1]
   return render_template('learn_home.html', object=object)


# FUNCTIONS



# RUN
if __name__ == '__main__':
   app.run(debug = True)
   
