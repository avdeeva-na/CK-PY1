list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
max_index = list_numbers[0]
for current_index in list_numbers:
   if current_index > max_index:
        max_index = current_index
# list_numbers[0], max_index = list_numbers[-1], max_index
# max_index = list_numbers.index(max(list_numbers))
# list_numbers[-1],list_numbers[max_index] =  list_numbers[max_index], list_numbers[-1]
print(list_numbers)

