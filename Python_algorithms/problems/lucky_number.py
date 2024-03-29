# Напишите код, который проверяет, счастливое это число или нет. В математике счастливым числом называют такое число,
# у которого, если постоянно возводить в квадрат и складывать все цифры числа и так раз за разом, в конце получится
# единица.

# считаем сумму квадратов цифр числа
def squared(n):
    # на старте она равна нулю
    result = 0
    # пока есть цифры в числе
    while n > 0:
        # получаем последнюю цифру
        last = n % 10
        # возводим её в квадрат и прибавляем к сумме
        result += last * last
        # отбрасываем последнюю цифру
        n = n // 10
    # выводим результат
    print(result)
    # возвращаем сумму
    return result


# проверяем, как работает функция
print(squared(19))


# проверяем, счастливое ли число
def isHappy(n):
    # запоминаем, с чего мы начали
    start = n
    # сумма на старте равна нулю
    result = 0
    # пока не получим единицу — выполняем цикл
    while result != 1:
        # получаем сумму квадратов цифр
        result = squared(n)
        # делаем её новым стартовым числом
        n = result
        # если сумма совпала с тем, что было — мы зациклились
        if result == start:
            print('Всё зациклилось')
            # выходим из функции
            return False
    # если дошли сюда — число счастливое
    return True


# число для проверки
test = 20

# проверяем, счастливое ли число и выводим ответ
if isHappy(test):
    print('Это счастливое число')
else:
    print('Это не счастливое число')
