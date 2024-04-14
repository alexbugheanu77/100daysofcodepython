# Generate a safe password to use
import random
import string

print("Welcome to the PyPassword Generator!")

password = ''

letters = list(string.ascii_lowercase + string.ascii_uppercase) #get alphabet as a string
numbers = [str(number) for number in range(0,10)]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# user inputs:
nr_letters = int(input("How many letters would you like in you password?\n>"))
nr_symbols = int(input("How many symbols would you like?\n>"))
nr_numbers = int(input("How many numbers would you like?\n>"))

#in functie de cate caractere introduce userul noi luam aleator cate are nevoie si le stocam in variabile separate

random_let = random.sample(letters, nr_letters)
random_num = random.sample(numbers, nr_numbers)
random_sym = random.sample(symbols, nr_symbols)

#le punem pe toate intr-o singura lista si le amestecam
new = random_let + random_num + random_sym
random.shuffle(new)

#returnam parola intr-un string
for i in new:
    password = password+ i
print(f"Your password is: {password}")