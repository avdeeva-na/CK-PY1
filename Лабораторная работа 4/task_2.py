def get_count_char(str_):
    dictionary = {} # TODO посчитать количество каждой буквы в строке в аргументе str_
    str_ = str_.lower()
    total_count = 0
    for letter in str_:
        if letter.isalpha():
            dictionary[letter] = dictionary.get(letter, total_count) + 1
    return dictionary

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
