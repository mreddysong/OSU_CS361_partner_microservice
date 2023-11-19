#adapted from https://www.youtube.com/watch?v=3QiPPX-KeSc
#Tech With Tim
#"Python Socket Programming Tutorial, April 5, 2020

import socket

HEADER = 64
PORT = 5051
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(64).decode(FORMAT))

while True:
    input("Enter input:")
    send("Hello")
