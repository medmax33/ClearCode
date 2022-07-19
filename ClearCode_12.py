1.
count = self.size
while count > 0:
    if self.slots[index] is None:
        return index
    count -= 1
// инициализация переменной непосредственно перед циклом, ранее она была инициализирована в самом начале метода

2.
def __init__(self, f_len):
    self.__filter_len = f_len
    # создаём битовый массив длиной f_len ...
    self.__random_digit_1 = 17
    self.__random_digit_2 = 223
    self.bitarray = 0
    self.__hash_zero = 0
// инициализация приватных атрибутов класса в конструкторе

3.
def red_or_green(track):
    i = 0
    for i in range(len(track)):
        if track[i][1] <= 0 or track[i][2] <= 0:
            return True
        else:
            return False
// вывел процедуру в отдельную функцию со своим счетчиком и сквозным массивом

4.
discount: int = 0
for _ in range(disc_block):
    discount += price_discount[_][2]
return discount
// инициализация discount перед циклом и вывод результата

5.
def distance_array(s: str, line: int, column: int):
    array: list = []
    start: int = 0
    finish: int = 0
    for _ in range(line):
        finish = start + column
        array.append(s[start:finish])
    start, finish = -100
    return array
// вывел процедуру в отдельную функцию, чтобы ограничить видимость start finish

6.
class LinkedList:

    def __init__(self):
        self.__head = None
        self.__tail = None
// приватные переменные класса

7.
class LinkedList:

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.node = None
// инициализация переменной node, используемой в дальнейшем

8.
def __str__(self):
    self.__it = []
    self.__ke = []
    self.__va = []
    for i in range(self.size):
        self.__it.append(i)
        self.__ke.append(self.slots[i])
        self.__va.append(self.values[i])
    return f"{self.__it}->[{self.__ke}]->{self.__va}"
// сделал приватные переменные для вывода, ранее они были глобальные

9.
def hash_fun(self, key: str):
    summa = 0
    for letter in key:
        summa += ord(letter)
    index = summa % self.size
    summa = -1000
    count = self.size
// ограничил использование переменной summa пределами функции

10.
def rotation(queue: list, n: int) -> list:
    for _ in range(n):
        queue.enqueue(queue.dequeue())
    return queue
// вывел повторяющуюся операцию в отдельный метод класса

11.
class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc
// приватная переменная при инициализации класса

12.
class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.__slots = [None] * self.size
// __slots используется только в рамках конкретного класса

13.
def put(self, value):
    self.__index = self.seek_slot(value)
    if self.__index is not None:
        self.slots[self.__index] = value
        return self.__index
    return None
// сделал приватным индекс для методов класса

14.
def union(self, set2):  #
    # объединение текущего множества и set2
    result_powerset = PowerSet()
// ранее result_powerset инициализировался в целом для всего класса

15.
class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        # создаём битовый массив длиной f_len ...
        self.random_digit_1 = 17
        self.random_digit_2 = 223
        self.bitarray = 0
        self.__hash_zero_1 = None
        self.__hash_zero_2 = None

    def hash1(self, str1):
        for _ in str1:
            code = ord(_)
            self.__hash_zero_1 = (self.__hash_zero_1 * self.random_digit_1 + code) % self.filter_len
        return self.__hash_zero_1
// объявил приватные переменные hash_zero_1 и hash_zero_2
// они используются в нескольких методах