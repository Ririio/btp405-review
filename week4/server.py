import socket

if __name__ == '__main__':
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  server_socket.bind(('localhost', 8080))

  server_socket.listen(5)

  print('Server is listening...')

  client_socket, client_address = server_socket.accept()

  print(f'A connection has been established with {client_address}')

  response = client_socket.recv(1024)

  print(response.decode())

  client_socket.send(b'Hello from server!')

  client_socket.close()