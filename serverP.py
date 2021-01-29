import socket
import threading

af = input("Local or public(1/2): ")
if af == "1":
    af = socket.AF_INET
elif af == "2":
    socket.AF_INET6

s = input("IP Addres : ")

HEADER = 64
PORT = 5050
SERVER = s
ADDR = (SERVER, PORT)
FORMAT  ="utf-8"
D_M = "MISS!"
loop = True

server = socket.socket(af, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(_conn, _addr):
    print(f"[NEW CONNECTION] {_addr} connected.")

    connected = True
    while connected:
        msg_len = _conn.recv(HEADER).decode(FORMAT)
        if msg_len:
            msg_len = int(msg_len)
            msg = _conn.recv(msg_len).decode(FORMAT)
            if msg == D_M:
                connected = False

            print(f"[FROM {_addr}] {msg}")
            _conn.send("received".encode(FORMAT))

    _conn.close()



def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    
    while loop:
        _conn, _addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(_conn, _addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]: {threading.activeCount() - 1}")

print("[STARTING]: server is booting...")
start()

