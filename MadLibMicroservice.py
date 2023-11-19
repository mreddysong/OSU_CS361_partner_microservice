#adapted from https://www.youtube.com/watch?v=3QiPPX-KeSc
#Tech With Tim
#"Python Socket Programming Tutorial, April 5, 2020

import socket
import threading
import random

HEADER = 64
PORT = 5051
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print("New connection to server")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            print(f"Server received {msg}")
            if msg == "Hello":
                random_number = str(random.randint(1, 8))
                conn.send(random_number.encode(FORMAT))

def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

print("Starting server...")
start()



