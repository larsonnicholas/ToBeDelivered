import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5928

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))

def clientHandler(conn, addr):
    print(f"New Connection from: {addr}.")

    while True:
        command = conn.recv(128).decode('utf-8')
        print(f"From {addr}: {command}")
        if "!close" in command:
            break
        elif not command or command == "": 
            break
        okState = "OK".encode('utf-8')
        conn.send(okState)
    print(f"Connection {addr} closed.\n")
    conn.close()

def serverListen():
    try:
        sock.listen()
    except KeyboardInterrupt:
        sock.close()
    print(f"{HOST}:{PORT}")
    while True:
        conn, addr = sock.accept()
        thread = threading.Thread(target=clientHandler, args=(conn, addr))
        thread.start()
        print(f"Connection Started... Active Threads: {threading.active_count()}")

try:
    serverListen()
except KeyboardInterrupt:
    sock.close()

