import socket
import threading



SERVER_ID = '127.0.0.1'
SERVER_PORT = 45678

nickname = input("Enter your nickname: ")

client_socket = socket.socket()
client_socket.connect((SERVER_ID, SERVER_PORT))


# Function to continuously receive messages from the server.
def receive_message():
    while True:
        try:
            # Receive message from server
            message = client_socket.recv(1024).decode()
            # If the message is a prompt for nickname, send the chosen nickname
            if message == "Nickname":
                client_socket.send(nickname.encode())
            else:
                print(message)

        except:
            print("Error!!!")
            client_socket.close()
            break


# Function to continuously input and send messages to the server.
def write_message():
    while True:
        # Input a message from the user
        message = f"{nickname} -> {input()}"
        # Send the message to the server
        client_socket.send(message.encode())



# Create a thread to receive messages from the server
receive_thread = threading.Thread(target=receive_message)
receive_thread.start()

# Create a thread to input and send messages to the server
write_thread = threading.Thread(target=write_message)
write_thread.start()