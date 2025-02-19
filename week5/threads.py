import threading
import time

def download_file(file_name: str, lock: threading.Lock) -> None:
  with lock:
    print(f'Downloading {file_name}')
    time.sleep(5)
    print(f'Finished Downloading {file_name}')

if __name__ == '__main__':
  files = ['file1.zip', 'file2.zip', 'file3.zip']
  threads = []  
  lock = threading.Lock()

  for file_name in files:
    thread = threading.Thread(target=download_file, args=(file_name, lock,))
    threads.append(thread)
    thread.start()

  for thread in threads:
    thread.join()

  print('Download Complete')
  