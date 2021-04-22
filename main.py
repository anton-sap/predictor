import numpy as np

ran_range_min = 1   # Устанавливаем минимум диапазона для рандомайзера
ran_range_max = 100    # Устанавливаем максимум диапазона для рандомайзера

count = 0                           # счетчик попыток
number = np.random.randint(ran_range_min, ran_range_max)   # загадали число
print(f"Загадано число от {ran_range_min} до {ran_range_max}")


def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count += 1
        predict = np.random.randint(ran_range_min, ran_range_max) # предполагаемое число
        if number == predict:
            return count    # выход из цикла, если угадали


def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''

    count = 0

    predict = np.random.randint(ran_range_min, ran_range_max)

    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return(count)   # выход из цикла, если угадали


def game_core_v3(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''

    count = 0

    low = ran_range_min
    high = ran_range_max

    while True:
        count += 1
        predict = (low + high) // 2

        if number == predict:
            break
        elif number > predict:
            low = predict + 1
        else:
            high = predict - 1

    return(count) # выход из цикла, если угадали


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''

    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))

    for number in random_array:
        count_ls.append(game_core(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


score_game(game_core_v3)
