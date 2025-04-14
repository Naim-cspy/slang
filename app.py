from flask import Flask, render_template, request

# Create a Flask app instance
app = Flask(__name__)

# Define a route and a view function
@app.route('/')
def main():
    return render_template('game.html')  # Render the game template as the homepage

# Start the game route
@app.route('/start_game', methods=['GET', 'POST'])
def start_game():
    if request.method == 'POST':
        score = 0
        name = request.form.get('name', '').strip()
        if not name:
            return "Name is required!", 400

        # Question 1
        jaweb1 = request.form.get('question1', '').strip().upper()
        if jaweb1 in ["MA ELE JLEDE", "MA ELE JALAD"]:
            score += 1

        # Question 2
        jaweb2 = request.form.get('question2', '').strip().lower()
        if jaweb2 in ["ana ma3ak", "jeye", "ana jeye", "ana ma3ak jeye", "ana jeye ma3ak", "bfout ma3ak", 
                      "ba3mel hal shi", "b3mel hal shi", "b3mel hal shi ma3ak", "b3mel hal shi jeye", 
                      "brou7", "brou7 ma3ak", "brou7 jeye", "brou7 ma3ak jeye"]:
            score += 1

        # Question 3
        jaweb3 = request.form.get('question3', '').strip().lower()
        if jaweb3 in ["nfokho", "nfekho"]:
            score += 1

        # Question 4
        jaweb4 = request.form.get('question4', '').strip().lower()
        if jaweb4 in ["mukhtal 3a2liyan", "mokhtal 3aqliyan", "mokhtal 3a2li", "mokhtal 3aqli", "mokhtal bi 3a2lo", 
                      "mokhtal 3aqli", "mahboul", "mastoul"]:
            score += 1

        # Question 5
        jaweb5 = request.form.get('question5', '').strip().lower()
        if jaweb5 in ["shou beke", "ashou beke"]:
            score += 1

        # Final result
        result = f"Your final score is {score} out of 5. You got {score / 5 * 100}% correct."
        return render_template('result.html', result=result, name=name)

    return render_template('game.html')

# Run the app if this file is executed
if __name__ == '__main__':
    app.run(debug=True)