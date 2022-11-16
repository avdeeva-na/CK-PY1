import random
from random import sample
import string
def get_random_password(length=8) -> str:
    population_ = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return "".join(random.sample(population_, length))
print(get_random_password())

