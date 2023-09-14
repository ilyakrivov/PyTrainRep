def square_calculate():
    global square_sum
    for num in square_all:
        square_sum += num
    return square_sum  # Возвращаем сумму площадей

def pl_calc(count_room):
    while count_room > 0:
        try:
            weight_room = float(input("Введите длину: "))
            height_room = float(input("Введите ширину: "))
            result = weight_room * height_room
            print('Площадь комнаты ', result, ' метров квадратных')
            square_all.append(result)
            count_room -= 1

        except ValueError:
            print('Некорректно введены данные, формат : Ширина , Длина ')
            return pl_calc(count_room)

    return square_calculate()  # Возвращаем сумму площадей после завершения цикла

def total_square():
    print('Общая площадь квартиры: ', square_sum)

square_all = []
square_sum = 0  # Инициализируем сумму площадей
count_room = int(input('Введите количество комнат: '))

if __name__ == "__main__":
    total = pl_calc(count_room)  # Получаем сумму площадей
    total_square()  # Выводим сумму площадей
