from flask import Flask, request, Response
import random

app = Flask(__name__)

@app.route('/console', methods = ['GET'])
def get_console():
    console = ['Playstation 4', 'Playstation 5', 'PC', 'XBOX Series X', 'Nintendo Switch']
    randconsole = random.randint(0, 4)
    return Response(console[randconsole], mimetype= 'text/plain')

if __name__ == '__main__':
    app.run(port = 5001, host = '0.0.0.0')