from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/getconsolegame', methods = ['GET'])
def get_consolegame():
    console = requests.get('http://service2:5001/console').text
    game = requests.get('http://service3:5002/game').text
    generate = console + ',' + game
    play = requests.post ('http://service4:5003/post/consolegame', data = generate).text
    return render_template('home.html', title = 'Random game and console generator', console = console, game = game, play = play)

if __name__ == '__main__':
    app.run(port = 5000, debug = True, host = '0.0.0.0')