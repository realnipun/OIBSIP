# server.py
import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Received: {message}")
                broadcast(message, client_socket)
            else:
                break
        except:
            continue

def broadcast(message, current_socket):
    for client in clients:
        if client != current_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                clients.remove(client)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5555))
server.listen(5)
clients = []

print("Server started. Waiting for connections...")

while True:
    client_socket, addr = server.accept()
    print(f"Connection from {addr}")
    clients.append(client_socket)
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
