from random import randint
def get_unique_list_numbers() -> list[int]:
     list_ = []
     while len(list_) < 16:
          return set([randint(-10, 10) for i in range(16)]) # TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
