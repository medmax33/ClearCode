1.
a: int
b: int
c = int(a / b)
// приведение результата деления к целочисленному

2.
a: int
b: int
try:
    c = int(a / b)
except ZeroDivisionError:
    print('Zero Division')
// проверка деления на ноль


3.
votes: list
percentage: list = []
total_votes: int
for current_vote in votes:
    percentage.append(round((current_vote / total_votes) * 100, 3))
// округление результата деления до трех знаков после запятой

4.
# calculate what light now on current TL
try:
    red_or_green = distance % (track[i][1] + track[i][2])
except ZeroDivisionError:
    print('tracks are Zero')
// проверка деления на ноль

5.
# check assertion in arrays
h1: int
array1: list
assert h1 == len(array1), 'h1 not equal len s1'
// проверка сообтветсвия введенной константы длины массива реальной длине массива


6.
discount_block: int = n // 3
// целочисленное деление

7.
sr_ar = int(sum(array) / len(array) + 0.5)
// округление в большую сторону

8.
continue_case = k[0] + i < 0 or k[0] + i >= h
if continue_case:
    continue
// примекнение булевой пеерменной


9.
distance += track[i][0]
assert distance < 10E10, 'distance too long'
// проверка на слишком большое значение длины

10.
a: int
b: int
d: float
c = round(a / b, 3)
d = round(d, 3)
c_bigger_d: bool = c > d
// применение булевой переменной

11.
answer_dictionary = {'1', '2', '3', '4', '5'}
if c == answer_dictionary[0]:
    return new_line.add(val)
elif c == answer_dictionary[1]:
    return new_line.delete(int(val))
elif c == answer_dictionary[2]:
    return new_line.give_value(int(val))
elif c == answer_dictionary[3]:
    return new_line.undo()
elif c == answer_dictionary[4]:
    return new_line.redo()
else:
    return new_line.current()
// использование словаря констант для множественного выбора

12.
candidate_1 = str(round((candidate_1_vote / total_votes) * 100, 3))
candidate_2 = str(round((candidate_2_vote / total_votes) * 100, 3))
if candidate_1 > candidate_2:
    print('candidate 1 won')
else:
    print('candidate 2 won')
// округление вещественных результатов расчетов, приведение их к строковым значениям и сравнение