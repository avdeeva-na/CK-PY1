from random import choice
from random import sample
import string
def get_random_password() -> str:
    let_upp = string.ascii_uppercase
    let_low = string.ascii_lowercase
    digits = string.digits
    population_ = [str(digits) for digits in range(9)]
    population_.append(let_upp)
    population_.append(let_low)
    population_ = ''.join(population_)
    password = sample(population_,8)
    return password
print(get_random_password())

