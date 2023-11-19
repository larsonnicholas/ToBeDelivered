import socket
import os
from datetime import datetime

#HOST = "134.197.34.36"
HOST = "127.0.1.1"
PORT = 5928

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST,PORT))

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
        return (fileName, fileSize, fileExt, timeUpload.strftime(formatDate)) 

def transferFile(filePath):
    metadata = fileMetadata(filePath)
    print(metadata)
    if serverMessage("!SEND"):
        None
        
def serverMessage(data):
    data = data.encode('utf-8')
    dataLen = len(data)
    padding = " "* (128 - dataLen)
    client.send(data)
    client.send(padding.encode('utf-8'))
    serverState = client.recv(2).decode('utf-8')
    if serverState != "OK":
        return False
    else: 
        return True

def serverFileData(data):
    data = data.encode('utf-8')
    dataLen = len(data)
    padding = " "* (128 - dataLen)
    client.send(data)
    client.send(padding.encode('utf-8'))
    client.accept()

def disconnectServer():
    client.send(b"!close")

try:
    transferFile("test.txt")
except Exception as e:
    print(e)
disconnectServer()