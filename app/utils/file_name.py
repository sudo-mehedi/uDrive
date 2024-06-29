from werkzeug.utils import secure_filename
from typing import List
import string
import random


def rand_char( n: int)-> str:
    return ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(n))


def unique_name(name: str):
    name = secure_filename(name)
    name = name.split('.')
    ext = name.pop()
    return f"{'.'.join(name)}_{rand_char(5)}.{ext}"



