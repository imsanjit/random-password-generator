import random
import string

def passwordGenerator(passwordLength, numberOfPassword):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    print(f"Here is your password: \n")
    for x in range(0, numberOfPassword):
        char_U = random.choice(string.ascii_uppercase)
        char_L = random.choice(string.ascii_lowercase)
        char_D = random.choice(string.digits)
        char_P = random.choice(string.punctuation)
        main_char = char_D + char_U + char_L + char_P
        password = main_char
        for number in range(0, passwordLength-4):
            pass_char = random.choice(chars)
            password +=  pass_char
        print(password)
        


passwordGenerator(9,6)
