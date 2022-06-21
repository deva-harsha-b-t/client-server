import socket
import threading

PORT = 9090
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "disconnect"

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(ADDR)


def send_mess(conn, addr):
    name = input("Enter your name: ")
    message = input()
    while message != DISCONNECT_MESSAGE:
        message = f"[{name}] {message}"
        msg = message.encode(FORMAT)
        conn.send(msg)
        message = input()
    conn.close()


def recv_mess(conn, addr):
    connected = True
    while connected:
        mess_ = conn.recv(HEADER).decode(FORMAT)
        if mess_:
            if mess_ == DISCONNECT_MESSAGE:
                connected = False
            print(f"{mess_}")
    conn.close()


def handle_conn(conn, addr):
    print(f"[connection : {addr} connected]")
    sendThread = threading.Thread(target=send_mess, args=(conn, addr))
    recvThread = threading.Thread(target=recv_mess, args=(conn, addr))
    sendThread.start()
    recvThread.start()


def start():
    serverSocket.listen()
    print(f"[Server {SERVER} is listening]")
    conn, addr = serverSocket.accept()
    handle_conn(conn, addr)


print("[--- server is starting ---]")
start()
