main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

_str = "".join(main_str.split())
_str = main_str.lower()

dict = {}
def get_count_char(str_):
    for char in _str:
        if char.isalpha():
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1

    return dict

print(get_count_char(main_str))
