import socket
import pickle


if __name__ == '__main__':
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


  PORT = 8000
  server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  server_socket.bind(('localhost', PORT))
  server_socket.listen(5)

  print('Server is listening...')

  client_socket, client_address = server_socket.accept()

  print(f'Connection Established {client_address}')

  serialized_data = pickle.loads(client_socket.recv(1024))
  print(f'Received Data: {serialized_data}')

  client_socket.close()

  
