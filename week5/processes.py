import time
from multiprocessing import Process

def calculate_num(nums):
  for num in nums:
    print(f'Square of {num} is {num**2}')
    time.sleep(3)

if __name__ == '__main__':
  nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  processes = []

  for i in range(2):
    p = Process(target=calculate_num, args=(nums[i::2],))
    processes.append(p)
    p.start()

  for p in processes:
    p.join()

  print('All calculations are complete')