import socket
import pickle

if __name__ == '__main__':
  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  try:
    PORT = 8000
    client_socket.connect(('localhost', PORT))

    print(f'Connection establish at Port: {PORT}')

    book = {'name': 'Lord of the Rings', 'author': 'J.R.R. Tolkien'}

    print(f'Sending Data: {book}')
    client_socket.send(pickle.dumps(book))

  except socket.error:
    print('Socket is not listening')

  client_socket.close()