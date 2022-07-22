3.1.
1.
def Keymaker(k: int) -> str:
    # определение замены в цикле генерации ключа
    trigger = ''.maketrans({'1': '0', '0': '1'})

2.
def Football(f: list, n: int) -> bool:
    # сначала проверяем на непустой список, далее идет тело программы
    if f:
        k: list = []
        m: list = []

3.
# перебор основного списка и сравнение его с упорядоченным
for i in range(n):
    if f[i] != f_up[i] and f[i] > f[i + (1 if i < n - 1 else 0)]:
        k.append(i)
        m.append(1)
    elif f[i] != f_up[i]:
        k.append(i)
        m.append(0)
    else:
        m.append(0)

4.
# проверка окончательного результата
# при длине массива = 0 условие не сохраняется
# при длине = 2 условие сохраняется
if len(k) == 0:
    return False
elif len(k) == 2:
    return True
# при дополнительном условии и наличии 0 в результирующем массиве
# условие сохраняется
elif len(k) > 2 and 0 not in m[k[0]:k[-1]]:
    return True
else:
    return False

5.
def white_walkers(village: str) -> bool:
    # для проверки задачи создаем массив и передаем в него
    # только числовые символы из строки
    ind = []

    for i in range(len(village)):
        if '1' <= village[i] <= '9':
            ind.append(i)
    if len(ind) < 2:
        return False

6.
# сравнение соседних значений числовых символов результирующего массива
for i in range(len(ind) - 1):
    if int(village[ind[i]]) + int(village[ind[i + 1]]) == 10 and village[ind[i]:ind[i + 1] + 1].count('=') != 3:
        return False
return True

7.
# служебная функция преобразования входящего массива
# на выходе получаем суммы чисел входного массива
def Transform(a: list) -> list:
    b: list = []

    for i in range(len(a)):
        for j in range(len(a) - i):
            k = i + j
            b.append(max(a[j:k + 1]))

    return b


3.2.
1.
def fill_field(N: int, M: int, battalion_pair: list) -> list:
    # тут комментарий не нужен
    # fill whole field with '0' and '1' - where battalion fall
    state_square = []  # whole field M*N
    for x in range(M):
        row = []
        for y in range(N):
            if (y, x) in battalion_pair:
                row.append(1)
            else:
                row.append(0)
        state_square.append(row)
    return state_square

2.
# сделаем общий комментарий про проверку входных значений
# check if len of arrays dosnt match
if N != len(ids) or N != len(salary):
    return [0, 0, 0]

# service ordered array of ids
ids_ordered = ids.copy()
ids_ordered.sort()

3.
# именование переменных с описанием сущности
def WordSearch(len: int, s: str, subs: str) -> list:
    formatted_lines = []
    result_array = []
    start = 0
