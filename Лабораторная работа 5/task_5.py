import random
from random import sample
import string
def get_random_password() -> str:
    ...  # TODO написать функцию генерации случайных паролей
    letters_l = string.ascii_lowercase
    letters_u = string.ascii_uppercase
    numbers = string.digits
    all = letters_u + letters_l + numbers
    password = random.sample(all, 8)
    return password

print(get_random_password())

