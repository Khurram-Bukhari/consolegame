from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/post/consolegame', methods=['POST'])
def console_game_combined():
    generate = request.data.decode('utf-8')
    console_game = generate.split(',')
    if console_game[0] == 'Playstation 4' and console_game[1] == 'Call of Duty: Black ops 1':
        play = 'Play Call of Duty: Black ops 1 on Playstation 4'
    elif console_game[0] == 'Playstation 4' and console_game[1] == 'God of War: Ragnorak':
        play = 'Play God of War: Ragnorak on Playstation 4'
    elif console_game[0] == 'Playstation 4' and console_game[1] == 'Counter-Strike: Global Offensive':
        play = 'Play Counter-Strike: Global Offensive on Playstation 4'
    elif console_game[0] == 'Playstation 4' and console_game[1] == 'Halo Infinite':
        play = 'Play Halo Infinite on Playstation 4'
    elif console_game[0] == 'Playstation 4' and console_game[1] == 'Mario Kart':
        play = 'Play Mario Kart on Playstation 4'
    elif console_game[0] == 'Playstation 5' and console_game[1] == 'Call of Duty: Black ops 1':
        play = 'Play Call of Duty: Black ops 1 on Playstation 5'
    elif console_game[0] == 'Playstation 5' and console_game[1] == 'God of War: Ragnorak':
        play = 'Play God of War: Ragnorak on Playstation 5'
    elif console_game[0] == 'Playstation 5' and console_game[1] == 'Counter-Strike: Global Offensive':
        play = 'Play Counter-Strike: Global Offensive on Playstation 5'
    elif console_game[0] == 'Playstation 5' and console_game[1] == 'Halo Infinite':
        play = 'Play Halo Infinite on Playstation 5'
    elif console_game[0] == 'Playstation 5' and console_game[1] == 'Mario Kart':
        play = 'Play Mario Kart on Playstation 5'
    elif console_game[0] == 'PC' and console_game[1] == 'Call of Duty: Black ops 1':
        play = 'Play Call of Duty: Black ops 1 on PC'
    elif console_game[0] == 'PC' and console_game[1] == 'God of War: Ragnorak':
        play = 'Play God of War: Ragnorak on PC'
    elif console_game[0] == 'PC' and console_game[1] == 'Counter-Strike: Global Offensive':
        play = 'Play Counter-Strike: Global Offensive on PC'
    elif console_game[0] == 'PC' and console_game[1] == 'Halo Infinite':
        play = 'Play Halo Infinite on PC'
    elif console_game[0] == 'PC' and console_game[1] == 'Mario Kart':
        play = 'Play Mario Kart on PC'
    elif console_game[0] == 'XBOX Series X' and console_game[1] == 'Call of Duty: Black ops 1':
        play = 'Play Call of Duty: Black ops 1 on XBOX Series X'
    elif console_game[0] == 'XBOX Series X' and console_game[1] == 'God of War: Ragnorak':
        play = 'Play God of War: Ragnorak on XBOX Series X'
    elif console_game[0] == 'XBOX Series X' and console_game[1] == 'Counter-Strike: Global Offensive':
        play = 'Play Counter-Strike: Global Offensive on XBOX Series X'
    elif console_game[0] == 'XBOX Series X' and console_game[1] == 'Halo Infinite':
        play = 'Play Halo Infinite on XBOX Series X'
    elif console_game[0] == 'XBOX Series X' and console_game[1] == 'Mario Kart':
        play = 'Play Mario Kart on XBOX Series X'
    elif console_game[0] == 'Nintendo Switch' and console_game[1] == 'Call of Duty: Black ops 1':
        play = 'Play Call of Duty: Black ops 1 on Nintendo Switch'
    elif console_game[0] == 'Nintendo Switch' and console_game[1] == 'God of War: Ragnorak':
        play = 'Play God of War: Ragnorak on Nintendo Switch'
    elif console_game[0] == 'Nintendo Switch' and console_game[1] == 'Counter-Strike: Global Offensive':
        play = 'Play Counter-Strike: Global Offensive on Nintendo Switch'
    elif console_game[0] == 'Nintendo Switch' and console_game[1] == 'Halo Infinite':
        play = 'Play Halo Infinite on Nintendo Switch'
    elif console_game[0] == 'Nintendo Switch' and console_game[1] == 'Mario Kart':
        play = 'Play Mario Kart on Nintendo Switch'
    else:
        play = 'Combination invalid'
    return Response(play, mimetype = 'text/plain')

if __name__ == '__main__':
    app.run(port = 5003, debug = True, host = '0.0.0.0')



