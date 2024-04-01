import socket
import threading


HOST = '127.0.0.1'
PORT = 45678


# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Server socket created")

# Bind the socket to the address and port
server_socket.bind((HOST, PORT))
server_socket.listen()
print(f"Server socket is listening {PORT}")

clients = []
nicknames = []


# Function to send a message to all connected clients.
def broadcast(message):
    # Write the message to the file
    with open("chat_log.txt", "a") as file:
        file.write(message.decode() + "\n")
          
    for client in clients:
        client.send(message)


# Function to handle messages from a single client.
def handle(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client_socket)
            clients.remove(client_socket)
            client_socket.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break


# Function to accept incoming connections from clients.
def receive():
    while True:
        # Accept a new connection
        client, address = server_socket.accept()
        print(f"Connected with {address}")

        client.send("Nickname".encode())
        nickname = client.recv(1024).decode()

        nicknames.append(nickname)
        clients.append(client)

        print(f"{nickname} connected" )

        broadcast(f"{nickname} joined the chat!".encode())


        # Create a new thread to handle messages from this client
        thread = threading.Thread(target=handle, args=(client, ))
        thread.start()


receive()