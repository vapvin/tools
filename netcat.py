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