import random 
import string 

print("----------Welcome to the ₱₳$$￦ఠℝↁ generator🔐!-----------")
#ask the user about the length of the password
#type convert so we can use math operators
length = int(input("enter the total number of characters for the password ** please consider your total number of characters matches the characters you enter ** : "))
print("")
num_letters = int(input("Enter the number of letters in the password : "))
num_numbers = int(input("Enter the number of numbers in the password : "))
num_symbols = int(input("Enter the number of symboles in the password : "))

if length != (num_letters + num_numbers + num_symbols) :
  print("Invalid input . the sum  of letters , numbers and symbols doesn't match the length of the password")
else : 
  #create a list of letters , numbers and symbols
  letters = string.ascii_letters
  numbers = string.digits
  symbols = string.punctuation

  #create a list of all charcters
  pass_chars = (
    random.choices(letters,k=num_letters) +  
    random.choices(numbers,k=num_numbers) + 
    random.choices(symbols,k=num_symbols)
  )

#shuffle the list of characters
random.shuffle(pass_chars)
#convert the list to string
password = "".join(pass_chars)
print("")
print("your password is :", password)
print("")
exit = input("press enter to exit..")