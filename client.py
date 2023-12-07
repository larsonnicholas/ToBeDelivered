import socket
import os
from datetime import datetime
from string import ascii_uppercase
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

#This import is only needed during WSL development, not useful in windows so delete once packing.
from string import ascii_lowercase
#

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
        raise Exception("Server Connection Timed Out")
    else:
        return client

def findFile(fileString):
    try:
        fileSize = os.path.getsize(fileString)
    except OSError as e:
        if e.errno == 2:
            print("Could not find file!")
            raise Exception("File Could Not Be Found.")
        elif e.errno in [13,1]:
            print("Incorrect permissions!")
            raise Exception("Incorrect File Permissions.")
        else:
            print("Unknown Error")
            raise Exception("Please try again later.")
    else:
        return fileSize
    
def fileMetadata(filePath):
        fileSize = findFile(filePath)
        #This line below isn't required, right?
        fileName = os.path.basename(filePath)
        fileInfo = os.path.splitext(filePath)
        fileName = fileInfo[0]
        fileExt = fileInfo[1]
        timeUpload = datetime.now()
        formatDate = '%m/%d/%Y %H:%M:%S'
        return (fileName, fileExt, str(fileSize), timeUpload.strftime(formatDate)) 

def transferFile(filePath, destination):
    metadata = fileMetadata(filePath)
    client = connectServer()
    #metadata.append(UserID)
    key = getPrivKey()
    if key != None:
        encryptedFile = encryptFile(filePath)
    if serverMessage("!SEND " + " ".join([i for i in metadata]) + " " + destination, client):
        try:
            with open(encryptedFile, "rb") as file:
                client.sendfile(file)
        except TimeoutError:
            #Display failed file transfer error window
            raise Exception("File Transfer Failed: Server Timed Out")
        client.close()

        #Database Information Entry Section
        #
        #
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

#Encryption functions

def generatePKey():
    key = get_random_bytes(32)
    with open("key.key", "wb") as file:
        file.write(key)

def getPrivKey():
    #Check in current directory
    currDir = os.getcwd()
    winPath = currDir + "\key.key"
    linuxPath = currDir + "/key.key"
    if os.path.exists(winPath) or os.path.exists(linuxPath):
        keyPath = ""
        if os.path.exists(winPath):
            keyPath = winPath
        else:
            keyPath = linuxPath

        with open(keyPath, "rb") as file:
            key = file.read()
        if len(key) != 32:
            raise Exception("Key length not appropriate for AES256")
        else:
            return key
    #Check in USB drive WINDOWS
    for drive in ascii_uppercase[:-24:-1]:
        keyPath = drive + ":\key.key"
        if os.path.exists(keyPath):
            with open(keyPath, "rb") as file:
                key = file.read()
            if len(key) != 32:
                raise Exception("Key length not appropriate for AES256")
            else:
                return key
    #This section is so the drive can still work if on WSL, this section should be removed when packaging.
    for drive in ascii_lowercase[:-24:-1]:
        keyPath = "/mnt/" + drive + "/key.key"
        if os.path.exists(keyPath):
            with open(keyPath, "rb") as file:
                key = file.read()
            if len(key) != 32:
                raise Exception("Key length not appropriate for AES256")
            else:
                return key
    #Private Key not found, don't encrypt the file and cancel transfer.
    raise Exception("Could Not Find Private Key.")

def encryptFile(filePath):
    fileName = os.path.basename(filePath)
    with open(filePath, "rb") as file:
        fileData = file.read()
    key = getPrivKey()
    if key:
        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag  = cipher.encrypt_and_digest(fileData)
        encryptedFile = fileName + "_enc"
        with open(encryptedFile, "wb") as file:
            [file.write(x) for x in (cipher.nonce, tag, ciphertext)]
        return encryptedFile
    else:
        raise Exception("Failed To Encrypt File. Please try again later.")
        
def decryptFile(filePath):
    fileName = os.path.basename(filePath)
    with open(filePath, "rb") as file:
        nonce, tag, ciphertext = [file.read(x) for x in (16, 16, -1)]
    key = getPrivKey()
    if key:
        cipher = AES.new(key, AES.MODE_EAX, nonce)
        fileData = cipher.decrypt_and_verify(ciphertext, tag)

        fileName = fileName.replace("_enc","")
        fileName = fileName + "_new"
        with open(fileName, "wb") as file:
            file.write(fileData)

try:
    #transferFile("CS450_Ch8.pdf", destination)
    decryptFile("CS450_Ch8_New.pdf")
except Exception as e:
    print(e)