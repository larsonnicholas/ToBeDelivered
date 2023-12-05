import socket
import os
from datetime import datetime
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

HOST = "134.197.34.36"
#HOST = "127.0.1.1"
PORT = 5928
UserID = ""
destination = HOST
BUFFER_SIZE = 4096

#CPE400 Lec29 has TLS Socket example, we should probably wrap the socket with TLS.
def connectServer():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(5)
    try:
        client.connect((HOST,PORT))
    except TimeoutError as e:
        #Display could not reach server error window
        raise e
    else:
        return client

def findFile(fileString):
    try:
        fileSize = os.path.getsize(fileString)
    except OSError as e:
        if e.errno == 2:
            print("Could not find file!")
        elif e.errno in [13,1]:
            print("Incorrect permissions!")
        else:
            print("Unknown Error")
        raise e
    else:
        return fileSize
    
def fileMetadata(filePath):
        fileSize = findFile(filePath)
        fileName = os.path.basename(filePath)
        fileInfo = os.path.splitext(filePath)
        fileName = fileInfo[0]
        fileExt = fileInfo[1]
        timeUpload = datetime.now()
        formatDate = '%m/%d/%Y %H:%M:%S'
        return (fileName, str(fileSize), fileExt, timeUpload.strftime(formatDate)) 

def transferFile(filePath, destination):
    metadata = fileMetadata(filePath)
    client = connectServer()
    #metadata.append(UserID)
    #encryptFile
    encryptedFile = filePath
    if serverMessage("!SEND " + " ".join([i for i in metadata]) + " " + destination, client):
        try:
            with open(encryptedFile, "rb") as file:
                client.sendfile(file)
        except TimeoutError as e:
            #Display failed file transfer error window
            raise e
        client.close()
    else:
        print("Didn't send...")
        
def serverMessage(data, client):
    dataLen = len(data)
    padding = " "*(128 - dataLen)
    data = data + padding
    print(data)
    client.send(data.encode('utf-8'))
    client.settimeout(5)
    serverState = client.recv(2).decode('utf-8')
    if serverState != "OK":
        return False
    else: 
        return True

try:
    transferFile("CS450_Ch8.pdf", destination)
except Exception as e:
    print(e)