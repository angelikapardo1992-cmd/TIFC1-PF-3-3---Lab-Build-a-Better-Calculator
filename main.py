def addmultiplenumbers(numbers):
  """Return the sum of a list of numbers."""
  return sum(numbers)


def multiplymultiplenumbers(numbers):
  """Return the product of a list of numbers."""
  result = 1
  for number in numbers:
    result *= number
  return result


def isitaninteger(num):
  """Return True if num is an integer value, else False."""
  if isinstance(num, bool):
    return False
  return isinstance(num, int) or (isinstance(num, float) and num.is_integer())


def isiteven(num):
  """Return True if num is an even integer, else False."""
  return isitaninteger(num) and int(num) % 2 == 0


def main():
  print("Hello learners!")


if __name__ == "__main__":
  main()
