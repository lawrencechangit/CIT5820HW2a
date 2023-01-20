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
        length_of_y = random.randint(1,100)
        y_string=random_string_generator(length_of_y)
        print("y is", y_string)
        m_y=hashlib.sha256(y_string.encode('utf-8')).hexdigest()
        x_bit=bin(eval("0x"+m_x))
        y_bit=bin(eval("0x"+m_y))
        if x_bit[-k:]==y_bit[-k:]:
            break
        else:
            continue

    x = x_string.encode('utf-8')
    y = y_string.encode('utf-8')
    return (x, y)






