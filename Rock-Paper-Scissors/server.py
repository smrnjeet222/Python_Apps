from _thread import *
import socket
import pickle
import sys
from game import Game

server = 'ip server is running on'
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()

print("Wating For Connection, Server Started")

connected = set()
games = {}
idCount = 0


def threaded_client(conn, p, gameid):
    global idCount
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()

            if gameid in games:
                game = games[gameid]
                
                if not data:
                    break
                else:
                    if data == 'reset':
                        game.resetWent()
                    elif data != 'get':
                        game.play(p, data)

                    reply = game
                    conn.sendall(pickle.dumps(reply))
            else:
                break
        except:
            break

    print("Lost Connection")
    try:
        del game[gameid]
        print("Closing Game", gameid)
    except:
        pass
    idCount -= 1
    conn.close()


while True:
    conn, addr = s.accept()
    print('Connected to :', addr)

    idCount += 1
    p = 0
    gameid = (idCount-1)//2

    if idCount % 2 == 1:
        games[gameid] = Game(gameid)
        print('Creating a new game....')
    else:
        games[gameid].ready = True
        p = 1

    start_new_thread(threaded_client, (conn, p, gameid))
