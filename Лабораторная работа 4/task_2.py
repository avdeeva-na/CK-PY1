def get_count_char(str_):
    dictionary = {} # TODO посчитать количество каждой буквы в строке в аргументе str_
    str_ = str_.lower()
    for letter in str_:
        if letter.isalpha():
            dictionary[letter] = dictionary.get(letter, 0) + 1
    return dictionary

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

def percent_for_chars(symbol):
    all_chars = sum(symbol.values())
    for i in symbol:
        symbol[i] = int((symbol[i] / all_chars) * 100)
    return symbol