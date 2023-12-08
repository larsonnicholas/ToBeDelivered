import socket
import threading
import os

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5928
BUFFER_SIZE = 4096

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))

def clientHandler(conn, addr):
    print(f"New Connection from: {addr}.")
    try:
        command = conn.recv(128).decode('utf-8')
        print(f"From {addr}: {command}")
        if not command:
            raise Exception("Empty Input")
        command = command.split()
        match command[0]:
            case "!SEND":
                conn.send("OK".encode('utf-8'))
                receiveFile(conn, command[1:])
            case "!GET":
                conn.send("OK".encode('utf-8'))
                sendFile(conn, command[1:])
            case "!LOGIN":
                conn.send("OK".encode('utf-8'))
                userLogin()
            case _:
                print("Command not recognized")
    except TimeoutError:
        print("Client timed out.")
    except Exception as e:
        print(e)
    print(f"Connection {addr} closed.\n")
    conn.close()

def receiveFile(conn, command):
    #store metadata in tables
    fileName = command[0] + command[1]
    with open(fileName, "wb") as file:
        data = conn.recv(BUFFER_SIZE)
        while data:
            file.write(data)
            data = conn.recv(BUFFER_SIZE)
        conn.shutdown(socket.SHUT_RD)
    print(f"File \"{fileName}\" received")

def sendFile(conn, command):
    #get file metadata, make sure user can access
    fileName = command[0]
    if os.path.isfile(fileName):
        with open(fileName, "rb") as file:
            conn.sendfile(file)
    else:
        raise Exception("Requested File Does Not Exist")

def userLogin():
    None

def serverListen():
    try:
        sock.listen()
    except KeyboardInterrupt:
        sock.close()
    print(f"{HOST}:{PORT}")
    while True:
        conn, addr = sock.accept()
        conn.settimeout(10)
        thread = threading.Thread(target=clientHandler, args=(conn, addr))
        thread.start()
        print(f"Connection Started... Active Threads: {threading.active_count()}")

while True:
    try:
        serverListen()
    except KeyboardInterrupt:
        sock.close()
        break