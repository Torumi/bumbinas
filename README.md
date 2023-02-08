# Падающие шарики

## Условие задачи
Рихард придумал двумерную симуляцию падения шариков на горизонтальную поверхность. Горизонтальная поверхность разделена на позиции по ширине щариков. Позиций на поверхности бесконечно много, и они пронумированы целыми числами, начиная от нуля в обе стороны(налево: -1, -2, -3, ...; направо: 1, 2, 3, ...)
В позицию 0 один за другим сбрасываются N шариков. Если шарик падает на поверхность, он остаётся в позиции, на которую упал. Если шарик падает в позицию *p*, где уже находится другой шарик, тогда он перемещается по таким правилам(смотр. изобр.):
1. Если в позиции справа *(p + 1)* точно под шариком есть свободное место, шарик перемещается на это место (изобр. случай A или B);
2. Если в позиции справа *(p + 1)* точно под шариком нет свободного места, но позиция слева *(p - 1)* свободна, шарик перемещается на это место (изобр. случай C);
3. Если обе соседние позиции заняты, шарик остаётся в позиции *p* (изобр. случай D).

![Falling rules](/docs/falling_rules.png)

Шарик перемещается по выше описанным до тех пор, пока не остановится. На изображении показано итоговое расположение первых 12 сброшенных шариков:

![Positions of first 12 balls](/docs/12_balls.png)

**Задание**: написать программу, которая для данного количества шариков посчитает, в какой позиции остановится последний шарик и сколько будет шариков в жтой позиции после падения последнего шарика

## Ввод
Вводится натуральное число N (кол-во сброшенных шариков, N ≤ 10<sup>18</sup> ).

## Вывод
В строке вывода программа выводит два натуральных числа - позиция, в которой остановился последний шарик и кол-во шариков в жтой позиции после падения последнего шарика.

## Примеры
* Ввод: 5	Вывод: 2 1
* Ввод: 8	Вывод: -1 2
* Ввод: 20	Вывод: 1 4

## Оригинальная формулировка
Оригинальное условие на латышском языке можно найти в [документе в репозитроии](docs/Novads2023_Bumbinas.pdf).

# Описание алогритма

## Определение
Примем, что итерация - промежуток между фиксациями шариков в позиции[0]
Начало иттерации - обновление фиксация шарика (будем считать таковие шарики за нулевые по счёту в итерации) в позиции[0]
Признак окончания иттерации и перехода к следующей - в позициях[0],[1],[-1] одинаковое кол-во шариков

## Закономерность позиции[0]
В позиции[0] фиксируются шарики, номера которых соответсвуют квадрату итерации =>
номер итерации можно считается по формуле `iteration = floor(sqrt(N))`, N - введённое число

Также, по этому признаку, если `N == iteration ** 2`, можно с точностью сказать, что последний шарик упал в позицию[0],
где находится iteration шариков

## Позиция шарика
В каждой итерации 1-ый шарик фиксируется в позиции[номер итерации], 2-ой шарик - в позиции[номер итерации - 1],  ... ,
i-ый шарик (последний в положительной позиции) в позиции[номер итерации - номер итерации + 1].

Последующие шарики падают в отрциательные позиции, начиная с позиции[-номер итерации], и стремясь к позиции[-1]:
позиции[-номер итерации], позиции[-номер итерации + 1], позиции[-номер итерации + 2], ... , позиции[-номер итерации + номер итерации - 1]

Таким образом, позиция падения шарика для положительной позиции считается по формуле `pos = iteration + 1 - (N- iteration**2)`

Если шарик по правилам падает в отрицательную позицию, предыдущая формула даёт неположительный результат в диапозоне [0; -(номер итерации - 1)].
По этому признаку, если pos <= 0, тогда позиция считается по формуле `pos = - iteration - pos1`,
где pos1 - полученный результат из прошлой формулы.

## Высота (кол-во шариков на позиции)
В каждой иттерации, 1-ый шарик фиксируется на высоте 1 (лежит на земле), 2-ой шарик фиксируется на высоте 2, ... ,
i-ый шарик (последний в положительной позиции) на высоте [номер итерации]

Отрицательные шарики также фиксируются на высотах от 1 до [номер итерации]

Зная позицию шарика и учитывая, что шарики (кроме нулевого)
в каждой итерации последовательно фиксируются в позициях[номер иттерации;1],
а затем в отрицательных позициях[-номер иттерации;-1],
выводится формула `heigth = iteration + 1 - abs(pos)`

## Формулы:
* N - введённое число
* iteration - номер итерации
* pos_positive - позиция, если по правилам положительная (pos_positive > 0)
* pos_negative - позиция, если по правилам отрицательная (pos_positive <= 0)
* heigth - высота (кол-во шариков на позиции)
  
* `iteration = floor(sqrt(N))`
* `pos_positive = iteration + 1 - (N - iteration**2)`
* `pos_negative = - iteration - pos_positive`
* `heigth = iteration + 1 - abs(pos)`