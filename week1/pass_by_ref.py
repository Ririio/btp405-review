from typing import List

def pass_by_ref(list: List[int | str]):
  list.append(6)

def change_val(val: int):
  val = 10

if __name__ == '__main__':
  print('Pass by reference')
  list = [1, 2, 3, 4, 5]

  print('Before:', list)
  pass_by_ref(list)
  print('After:', list)

  print('\nPass by value')
  val = 5
  print('Before:', val)
  change_val(val)
  print('After:', val)