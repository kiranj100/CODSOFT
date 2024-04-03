import random

length = int(input("Enter the length of the password: "))

all_alphabet = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            "@#$%&")

password = ""

for _ in range(length):
    random_index = random.randint(0, len(all_alphabet) - 1)
    password += all_alphabet[random_index]

print("Random Password is :", password)
