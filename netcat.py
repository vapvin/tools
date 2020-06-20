import sys
import socket
import getopt
import threading
import subprocess

listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((ip,port))

server.listen(5)

print '[*] Listening on %s:%d' % (ip, port)

def handle_client(client_socket):

    request = client_socket.recv(1024)

    print '[*] Received: %s' % request

    client_socket.send("ACK!")

    client_socket.close()