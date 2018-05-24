import string
import random


def pw_gen(pw_len = 4):
    option = (string.ascii_letters + string.digits + string.punctuation)
    return ''.join(random.choice(option) for _ in range(pw_len))

pw_len = int(input("Enter the length of the password you want:"))
print(pw_gen(pw_len))