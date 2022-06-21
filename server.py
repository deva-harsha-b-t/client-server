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


def send_mess(conn, msg):
    message = msg.encode(FORMAT)
    conn.send(message)


def handle_conn(conn, addr):
    print(f"[connection : {addr} connected]")

    connected = True
    while connected:
        mess_ = conn.recv(HEADER).decode(FORMAT)
        if mess_:
            if mess_ == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {mess_}")
        mssg = input("Enter message: ")
        send_mess(conn, mssg)
    conn.close()


def start():
    serverSocket.listen()
    print(f"[Server {SERVER} is listening]")
    while True:
        conn, addr = serverSocket.accept()
        thread = threading.Thread(target=handle_conn, args=(conn, addr))
        thread.start()
        print(f"[current connections: {threading.active_count() -1 }]")


print("[--- server is starting ---]")
start()
