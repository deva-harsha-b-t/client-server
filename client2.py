import socket
import threading

PORT = 9090
SERVER = "192.168.56.1"
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "disconnect"
ADDR = (SERVER, PORT)

print("[--- client strted ---]")

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(ADDR)


def send_mess():
    name = input("Enter your name: ")
    message = input()
    while message != DISCONNECT_MESSAGE:
        message = f"[{name}] {message}"
        msg = message.encode(FORMAT)
        clientSocket.send(msg)
        message = input()
    clientSocket.close()


def recv_mess():
    connected = True
    while connected:
        mess_ = clientSocket.recv(HEADER).decode(FORMAT)
        if mess_:
            if mess_ == DISCONNECT_MESSAGE:
                connected = False
            print(f"{mess_}")
    clientSocket.close


def start():
    sendThread = threading.Thread(target=send_mess, args=())
    recvThread = threading.Thread(target=recv_mess, args=())
    sendThread.start()
    recvThread.start()


start()
