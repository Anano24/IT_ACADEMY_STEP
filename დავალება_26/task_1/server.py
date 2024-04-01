import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Server socket created!")

HOST = '0.0.0.0'
PORT = 45678

server_socket.bind((HOST, PORT))
server_socket.listen()
print('Server socket is listening...')


while True:
    conn, addr = server_socket.accept()
    print(f'Connected by: {addr}')
    message = 'Server -> Connection successful'
    conn.sendall(message.encode())
    conn.close()