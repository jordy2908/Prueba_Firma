import random

def codigo(n = 4):
    all_char = '0123456789'
    index = len(all_char) + 0
    c = ''
    for _ in range(n):
        numeros = random.randint(0, index)
        c += all_char[numeros]
    return c