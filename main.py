#Pamela Vishka
def encode(password):
  pwEncoded = ""                      # empty string to store new pw

  for i in password:                  # iterates through each digit in password
    newNum = int(i) + 3               # adds 3 to each digit  
    if newNum == 10:
      newNum = 0                      # accounting for double digits (10, 11, 12)
    elif newNum == 11:
      newNum = 1
    elif newNum == 12:
      newNum = 2
    pwEncoded += str(newNum)          # adding each new digit to pwEncoded

  return pwEncoded


def decode(password): #this function decodes the password that was previously encoded
  original = ""
  for i in password:
    num = int(i) - 3
    if num == (-1):
      num = 9
    elif num == (-2):
      num == 8
    elif num == (-3):
      num = 7
      original += str(num)
    return original


if __name__ == "__main__":

  while True:
    print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n') #menu that is printed out
    option = int(input('Please enter an option: '))      # user input
    if option != 3:
          if option == 1: # encode password
            password = input("Please enter your password to encode: ")
            encodedPW = encode(password)
            print('Your password has been encoded and stored!')
          if option == 2:
            original = decode(encodedPW)
            print(f'The encoded password is {encodedPW}, and the original password is {password}')
          if option == 3: #quit
            break
