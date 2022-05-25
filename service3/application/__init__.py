from flask import Flask, request, Response
import random

app = Flask(__name__)

@app.route('/game', methods=['GET'])
def get_game():
    game = ['Call of Duty: Black ops 1', 'God of War: Ragnorak', 'Counter-Strike: Global Offensive', 'Halo Infinite', 'Mario Kart']
    randgame = random.randint(0, 4)
    return Response(game[randgame], mimetype= 'text/plain')

if __name__ == '__main__':
    app.run(port = 5002, debug = True, host = '0.0.0.0')