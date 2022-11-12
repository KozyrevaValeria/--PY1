from random import randint

def get_unique_list_numbers() -> list[int]:
    ...  # TODO написать функцию для получения списка уникальных целых чисел
    random_number = [randint(-10, 10) for _ in range(15)]
    unique_number = []
    for number in random_number:
        if number not in unique_number:
            unique_number.append(number)

    return unique_number

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
