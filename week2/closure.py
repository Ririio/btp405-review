def outer(x):
  def inner(y):
    return x + y
  return inner

if __name__ == '__main__':
  outer_func = outer(10)
  print(outer_func(20))