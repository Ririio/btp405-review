import socket

if __name__ == '__main__':
  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  try:
    client_socket.connect(('localhost', 8080))
    
    client_socket.send(b'Hello from Client')

    response = client_socket.recv(1024)
    print(response.decode())
  except socket.error:
    print('Socket is not listening')

  client_socket.close()