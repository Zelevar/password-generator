from string import ascii_letters as letters
import random

def generate(length) -> str:
    return ''.join(random.choice(letters) for i in range(length))

print(generate(64))