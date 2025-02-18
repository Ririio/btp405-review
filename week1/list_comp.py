if __name__ == '__main__':

  exponent = [num**2 for num in range(11) if num%2 == 0 and num != 0]
  print(exponent)

  multiplication = [num*3 for num in range(31) if num%3 == 0 and num != 0]
  print(multiplication)

  division = [int(num/2) for num in range(10) if num%2 == 0 and num != 0]
  print(division)
