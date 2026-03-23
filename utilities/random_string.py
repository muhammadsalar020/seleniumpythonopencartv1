import random
import string

def random_string_generator(size=8):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=size))