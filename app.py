from flask import Flask, render_template, request, redirect, url_for

# Create a Flask app instance
app = Flask(__name__)

# Define the questions and answers 
questions = [
    {"question": "shou ya3ne 'MEJ'?", "answers": ["MA ELE JLEDE", "MA ELE JALAD"]},
    {"question": "shou ma3na 'bshil'?", "answers": [
        "ana ma3ak", "jeye", "ana jeye", "ana ma3ak jeye", "ana jeye ma3ak",
        "bfout ma3ak", "ba3mel hal shi", "b3mel hal shi", "b3mel hal shi ma3ak",
        "b3mel hal shi jeye", "brou7", "brou7 ma3ak", "brou7 jeye", "brou7 ma3ak jeye"
    ]},
    {"question": "shou ya3ne 'NF5'?", "answers": ["nfokho", "nfekho"]},
    {"question": "shou ya3ne 'Mokh'?", "answers": [
        "mukhtal 3a2liyan", "mukhtal 3aqliyan", "mukhtal 3a2li", "mukhtal 3aqli",
        "mukhtal bi 3a2lo", "mokhtal 3a2liyan", "mokhtal 3aqliyan", "mahboul", "mastoul"
    ]},
    {"question": "shou ya3ne 'ashbike'?", "answers": ["shou beke", "ashou beke"]}
]

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the game page
@app.route('/game', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        user_answers = []
        score = 0
        for i, question in enumerate(questions):
            user_answer = request.form.get(f'question{i + 1}', '').strip().lower()
            user_answers.append(user_answer)
            if user_answer in [answer.lower() for answer in question['answers']]:
                score += 1
        return redirect(url_for('results', score=score, total=len(questions), user_answers=user_answers))
    return render_template('game.html', questions=questions)

# Route for the results page
@app.route('/results')
def results():
    score = request.args.get('score', 0, type=int)
    total = request.args.get('total', 0, type=int)
    user_answers = request.args.getlist('user_answers')
    print(f"Score: {score}, Total: {total}")
    return render_template('results.html', score=score, total=total, questions=questions, user_answers=user_answers)

# Run the app if this file is executed
if __name__ == '__main__':
    app.run(debug=True)
