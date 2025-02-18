def decorator(func):
  def wrapper(**args):
    print('Before calling the function')
    func(args)
    print('After calling the function')
  return wrapper

@decorator
def say_hello():
  print('Hello!')

@decorator
def hi_name(name):
  print(f'Hi, {name['name']}!')

if __name__ == '__main__':
  # say_hello()
  hi_name(name='John')
  # Unpack the string 'Done' into individual characters
  print(*'Done')