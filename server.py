import socket
from threading import Thread
import time
import os

IP_ADDRESS = '127.0.0.1'
PORT = 8050
SERVER = None
BUFFER_SIZE = 4096
CLIENTS = {}

def acceptConnection():
    global SERVER
    global client

    while True:
        client, addr = SERVER.accept()
        client_name = client.recv(4096).decode().lower()
        client[client_name] = {
            "client" : client,
            "address": addr,
            "connection_with": "",
            "file_name": "",
            "file_size": 4096
        }
        print(f"Connection Established with {client_name} : {addr}")
        
        thread = Thread(target = handleClient, args={client,client_name})
        thread.strat()
        
def setup():
    print ("\\t\t\t\t\t\tIP MESSENGER\n")
    
    global PORT
    global IP_ADDRESS
    global SERVER

    SERVER = socket . socket (socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind ( (IP_ADDRESS, PORT) )
    
    SERVER.listen(100)
    print("\t\t\t\tSERVER IS WAITING FOR INCOMMING CONNECTIONS...")
    print("\n")

    acceptConnection()

setup_thread = Thread(target=setup)
setup_thread.start()
