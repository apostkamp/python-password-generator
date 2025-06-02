import random
import string

def generate_password(length, complexity):
    if complexity == 'basic':
        chars = string.ascii_letters + string.digits
    elif complexity == 'intermediate':
        chars = string.ascii_letters + string.digits + string.punctuation
    elif complexity == 'advanced':
        chars = string.ascii_letters + string.digits + string.punctuation + ' '

    password = ''.join(random.choice(chars) for _ in range(length))

    return password

length = int(input("Enter password length: "))
complexity = input("Choose the complexity level (basic, intermediate, advanced): ")

password = generate_password(length, complexity)
print("Your password is: ", password)