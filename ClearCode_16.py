1.
def odometer(oxana: list) -> int:

    # Проверяем четность массива oxana
    if len(oxana) % 2 != 0:
        oxana.append(oxana[-2])

2.
# обязательная служебная функция по переформатированию массива batalion
# позволяет перегруппировать пары координат уменьшив их на еденицу
def refactor_battalion(battalion: list) -> list:
    # split battalion by pair
    battalion_pair = []  # battalion array split by pair of coordinate

    for k in range(0, len(battalion), 2):
        battalion_pair.append((battalion[k] - 1, battalion[k + 1] - 1))

    return battalion_pair

3.
def MadMax(N: int, Tele: list) -> list:
    # ОБЯЗАТЕЛЬНАЯ проверка равенства N и длины массива
    # если равенства нет, то функция отработает с ошибкой
    if N != len(Tele):
        return [0, 0, 0]

4.
# TODO - обязательно рефакторить массив в структуру Упорядоченный массив
for i in range(N):
    ind = ids.index(ids_ordered[i])
    salary[ind] = salary_ordered[i]

5.
def PatternUnlock(N: int, hits: list) -> str:
    if N != len(hits):
        return 'error'
    # TODO - вывести данные массивы в справочник вне данной функции
    d1: list = [2, 4, 6, 7, 9]
    d2: list = [1, 3, 5, 8]

6.
# НЕ УДАЛЯЙТЕ ЭТОТ МОДУЛЬ
# он используется в двух местах в расчете программы
def min3(a, b, c):
    if a <= b and a <= c:
        return a
    if b <= c:
        return b
    return c

7.
# данный класс описывает любого сотрудника в организации
class Employee:

# данный класс детализщирует характеристики сотрудника на испытательном сроке
class Trainee(Employee):

# класс сотрудника принятого в штат и работающего на основной зарплате
class Staff(Employee):

8.
def SumOfThe(n: int, data: list) -> int:

    # test if n equal length data
    if n != len(data):
        # TODO - изменить вывод функции при ошибке, сделать -1, этого достаточно
        return -1000000000000000000000000

9.
def TheRabbitsFoot(s: str, encode: bool) -> str:

    if encode:
        # TODO - обязательно сделать проверка на исключения в методе encryting
        return encrypting(s)
    else:
        return decrypting(s)

10.
def PrintingCosts(line: str) -> int:

    # в этом словаре хранится таблица подстановки символов
    # TODO - вынести словарь в отдельный модуль
    dictionary = {' ': 0, '!': 9, '"': 6, '#': 24, '$': 29, '%': 22,
                  '&': 24, '\'': 3, '(': 12, ')': 12, '*': 17, '+': 13,
                  ',': 7, '-': 7, '.': 4, '/': 10, '0': 22, '1': 19,
                  '2': 22, '3': 23, '4': 21, '5': 27, '6': 26, '7': 16,

11.
def BigMinus(s1: str, s2: str) -> str:
    # проверяем соотвествие друг другу входные переменные
    # не удалять первую проверку, можем получить исключение
    if s1 == s2:
        return '0'

    if s2 > s1:
        s1, s2 = s2, s1
    index: int = len(s1)
    s2 = s2.rjust(index, '0')

12.
# массив percentage представляет собой массив с расчетом процентов голосов
# для каждого кандидата
percentage = []
for _ in votes:
    percentage.append(round((_ / total_votes) * 100, 3))

# массив percent представляет собой упорядоченный массив percentage
# их нельзя объединять: в дальнейшем будем сравнивать очередность неупорядоченных
# и упорядоченных значений
percent = sorted(percentage, reverse=True)
