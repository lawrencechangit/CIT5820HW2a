import hashlib
import os
import random
import string

def random_string_generator(length):
    letters = string.ascii_uppercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def hash_collision(k):
    if not isinstance(k, int):
        print("hash_collision expects an integer")
        return (b'\x00', b'\x00')
    if k < 0:
        print("Specify a positive number of bits")
        return (b'\x00', b'\x00')

    # Collision finding code goes here
    x = b'\x00'
    y = b'\x00'

    length_of_x=random.randint(1,10)
    x_string=random_string_generator(length_of_x)
    m_x = hashlib.sha256(x_string.encode('utf-8')).hexdigest()

    while True:
        length_of_y = random.randint(1, 100000)
        y_string=random_string_generator(length_of_y)
        m_y=hashlib.sha256(y_string.encode('utf-8')).hexdigest()
        for i in range (256-k,255):
            x_int=int(m_x,16)
            y_int=int(m_y,16)
            if x_int[i]==y_int[i]:
                print(m_x[i])
                print(m_y[i])
                continue
            else: break
        break

    x = x_string.encode('utf-8')
    y = y_string.encode('utf-8')

    return (x, y)





