stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

# Type your code below
x_pos = stdform.find("x")
std_num = stdform[:x_pos]
power_pos = stdform.find("^")
power = stdform[power_pos + 1:]

def check_int(power):
  try:
      int(power_pos)
      return True
  except ValueError:
      return False

def validatation(stdform):
  validated_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "E", "x", ".", "-", "^"]
  val_present = all(elem in validated_chars for elem in stdform)
  if val_present:
    if (stdform.count(".") == 1 and stdform.count("x") == 1 and stdform.count("^") == 1 and check_int(power)):
      return True
    else:
      return False

if validatation(stdform):
  print(f"This number in E notation is {std_num}E{power}.")
else:
  print("Error converting to scientific E notation.")










