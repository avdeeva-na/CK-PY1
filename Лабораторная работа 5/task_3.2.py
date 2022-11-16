import random
from random import randint
def get_unique_list_numbers(start=-10, stop=10, size=15) -> list[int]:
     list_ = []
     while True:
          i = random.randint(start, stop)
          if i not in list_:
               list_.append(i)
          if len(list_) == 15:
               break
     return list_

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
