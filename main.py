"""
Testsst1

Определение
    Примем, что итерация - промежуток между фиксациями шариков в позиции[0]
        Начало иттерации - обновление фиксация шарика (будем считать таковие шарики за нулевые по счёту в итерации) в позиции[0]
        Признак окончания иттерации и перехода к следующей - в позициях[0],[1],[-1] одинаковое кол-во шариков

Закономерность позиции[0]
    В позиции[0] фиксируются шарики, номера которых соответсвуют квадрату итерации =>
        номер итерации можно считается по формуле iteration = floor(sqrt(N)), N - введённое число

    Также, по этому признаку, если N == iteration ** 2, можно с точностью сказать, что последний шарик упал в позицию[0],
        где находится iteration шариков

Позиция шарика
    В каждой итерации 1-ый шарик фиксируется в позиции[номер итерации], 2-ой шарик - в позиции[номер итерации - 1],  ... ,
        i-ый шарик (последний в положительной позиции) в позиции[номер итерации - номер итерации + 1].

    Последующие шарики падают в отрциательные позиции, начиная с позиции[-номер итерации], и стремясь к позиции[-1]:
        позиции[-номер итерации], позиции[-номер итерации + 1], позиции[-номер итерации + 2], ... , позиции[-номер итерации + номер итерации - 1]

    Таким образом, позиция падения шарика для положительной позиции считается по формуле pos = iteration + 1 - (N- iteration**2)

    Если шарик по правилам падает в отрицательную позицию, предыдущая формула даёт неположительный результат в диапозоне [0; -(номер итерации - 1)].
        По этому признаку, если pos <= 0, тогда позиция считается по формуле pos = - iteration - pos1,
        где pos1 - полученный результат из прошлой формулы.

Высота (кол-во шариков на позиции)
    В каждой иттерации, 1-ый шарик фиксируется на высоте 1 (лежит на земле), 2-ой шарик фиксируется на высоте 2, ... ,
        i-ый шарик (последний в положительной позиции) на высоте [номер итерации]

    Отрицательные шарики также фиксируются на высотах от 1 до [номер итерации]

    Зная позицию шарика и учитывая, что шарики (кроме нулевого)
        в каждой итерации последовательно фиксируются в позициях[номер иттерации;1],
            а затем в отрицательных позициях[-номер иттерации;-1],
                выводится формула heigth = iteration + 1 - abs(pos)

Формулы:
    N - введённое число
    iteration - номер итерации
    pos_positive - позиция, если по правилам положительная (pos_positive > 0)
    pos_negative - позиция, если по правилам отрицательная (pos_positive <= 0)
    heigth - высота (кол-во шариков на позиции)

    iteration = floor(sqrt(N))
    pos_positive = iteration + 1 - (N - iteration**2)
    pos_negative = - iteration - pos_positive
    heigth = iteration + 1 - abs(pos)
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
