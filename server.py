import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5928
BUFFER_SIZE = 4096

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))

def clientHandler(conn, addr):
    print(f"New Connection from: {addr}.")
    try:
        while True:
            command = conn.recv(128).decode('utf-8')
            print(f"From {addr}: {command}")
            if "!close" in command:
                break
            elif not command:
                break
            command = command.split()
            print(f"Split command: {command}")
            match command[0]:
                case "!SEND":
                    conn.send("OK".encode('utf-8'))
                    receiveFile(conn, command[1:])
                case "!LOGIN":
                    conn.send("OK".encode('utf-8'))
                    userLogin()
                case _:
                    print("Command not recognized")
                    continue
    except TimeoutError:
        print("Client timed out.")
    print(f"Connection {addr} closed.\n")
    conn.close()

def receiveFile(conn, command):
    #store metadata in tables
    fileName = command[0] + "_New" + command[2]
    with open(fileName, "wb") as file:
        data = conn.recv(BUFFER_SIZE)
        while data:
            if "!EOF".encode('utf-8') in data:
                print(data)
                data = data.strip("!EOF".encode('utf-8'))
                print(data)
                file.write(data)
                break
            else:
                file.write(data)
                print(data)
                data = conn.recv(BUFFER_SIZE)
    conn.send("OK".encode('utf-8'))
    print("File received")


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
        conn.settimeout(5)
        thread = threading.Thread(target=clientHandler, args=(conn, addr))
        thread.start()
        print(f"Connection Started... Active Threads: {threading.active_count()}")

try:
    serverListen()
except KeyboardInterrupt:
    sock.close()