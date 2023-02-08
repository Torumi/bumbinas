"""
Read documentation in README.md
"""

import math
from math import floor


def main(num_balls):
    # Закономерность позиции[0]
    iteration = floor(math.sqrt(num_balls)) # расчёт итерации
    if num_balls == iteration ** 2: # Если шарик нулевой в итерации, он находится в позиции 0 на высоте iteration
        return (0, iteration)

    # Позиция шарика
    pos = iteration + 1 - (num_balls - iteration ** 2)  # расчёт позиции шарика
    if pos <= 0:  # если pos <= 0, тогда расчёт отрицательной позиции шарика
        pos = - iteration - pos

    # Высота (кол-во шариков на позиции)
    heigth = iteration + 1 - abs(pos)  # расчёт высоты
    return (pos, heigth)


"""
Функция теста 
    Выполняет тест заданной функции с заданным списком параметров
    Записывает в лог ввод, вывод и время выполнения
"""
import time
from loguru import logger
import sys

logger.remove()
logger.add("tests.log", rotation="50 MB", backtrace=True, diagnose=True)  # Automatically rotate too big file
logger.add(sys.stdout, colorize=True, format="<green>{time:DD HH:mm:ss}</green> <level>{message}</level>",
           level='INFO')


def test_function(func, list_of_tests):
    for test_input in list_of_tests:
        start = time.time()
        result_pos, result_heigth = func(test_input)
        end = time.time()
        logger.info(f"Input: {test_input}   Output: {result_pos} {result_heigth}    Time:{end - start}")


if __name__ == '__main__':
    import random

    num_of_tests = 100000

    test_function(main, [5, 8, 20, 37, 155, 283])
    test_function(main, range(101))
    test_function(main, [random.randint(0, 10 ** 18) for _ in range(num_of_tests)])
