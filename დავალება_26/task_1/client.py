import socket



client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Client socket created!")

SERVER_IP = '127.0.0.1'
SERVER_PORT = 45678

client_socket.connect((SERVER_IP, SERVER_PORT))

received_msg = client_socket.recv(1024).decode()
print(received_msg)
client_socket.close()