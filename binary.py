my_list = list(range(1, 41025)) # условная БД
item = 992  # вводимые данные
tryCount = [0]  # Переменная tryCount объявлена как список для передачи по ссылке

def bin_search(my_list, item, tryCount):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = my_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
        tryCount[0] += 1  # Увеличиваем значение первого элемента списка tryCount

    return None

result = bin_search(my_list, item, tryCount)

if result is not None:
    print(f"Элемент {item} найден по индексу {result}, Количество затраченных попыток: {tryCount[0]}")
else:
    print(f"Элемент {item} не найден в списке.")
