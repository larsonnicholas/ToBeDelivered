import socket
import os
from datetime import datetime

HOST = "134.197.34.36"
#HOST = "127.0.1.1"
PORT = 5928
UserID = ""
destination = HOST
BUFFER_SIZE = 4096

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
        return (fileName, str(fileSize), fileExt, timeUpload.strftime(formatDate)) 

def transferFile(filePath, destination):
    metadata = fileMetadata(filePath)
    #metadata.append(UserID)

    #encryptFile
    if serverMessage("!SEND " + " ".join([i for i in metadata]) + " " + destination):
        with open(filePath, "rb") as file:
            while True:
                fileContents = file.read(BUFFER_SIZE)
                if not fileContents:
                    serverMessage("!EOF")
                    break
                if serverFileData(fileContents):
                    continue
                else:
                    print("Failed transfer")
                    break
    else:
        raise "File Transfer Failed!"
                
        
def serverMessage(data):
    data = data.encode('utf-8')
    print(data)
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
    dataLen = len(data)
    padding = " "* (BUFFER_SIZE - dataLen)
    client.send(data)
    client.send(padding.encode('utf-8'))
    okmsg = client.recv(2).decode('utf-8')
    if okmsg == "OK":
        return True
    else: 
        print("Did not receive OK signal from server")
        return False

def disconnectServer():
    serverMessage("!close")

try:
    transferFile("ExampleFile.txt", destination)
except Exception as e:
    print(e)
    disconnectServer()
disconnectServer()