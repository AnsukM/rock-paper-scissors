
from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

# ASCII art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Rock Paper Scissors</title>
    <style>
        body { font-family: Arial; text-align: center; margin-top: 50px; }
        pre { text-align: left; display: inline-block; }
        button { padding: 10px 20px; margin: 10px; font-size: 16px; }
        .result { margin: 20px; font-size: 24px; }
    </style>
</head>
<body>
    <h1>Rock Paper Scissors Game</h1>
    <form method="post">
        <button name="choice" value="0">Rock</button>
        <button name="choice" value="1">Paper</button>
        <button name="choice" value="2">Scissors</button>
    </form>
    {% if user_choice is not none %}
        <h2>Your Choice:</h2>
        <pre>{{ user_image }}</pre>
        <h2>Computer's Choice:</h2>
        <pre>{{ computer_image }}</pre>
        <div class="result">{{ result }}</div>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def play_game():
    user_choice = None
    computer_choice = None
    result = None
    user_image = None
    computer_image = None
    
    if request.method == 'POST':
        user_choice = int(request.form['choice'])
        computer_choice = random.randint(0, 2)
        
        user_image = game_images[user_choice]
        computer_image = game_images[computer_choice]
        
        if user_choice == computer_choice:
            result = "It's a Draw!"
        elif (user_choice == 0 and computer_choice == 2) or \
             (user_choice == 1 and computer_choice == 0) or \
             (user_choice == 2 and computer_choice == 1):
            result = "You Win!"
        else:
            result = "You Lose!"
    
    return render_template_string(HTML_TEMPLATE,
                                user_choice=user_choice,
                                user_image=user_image,
                                computer_image=computer_image,
                                result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

