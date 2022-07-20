1.
def test_1(self):
    self.assertEqual(ShopOLAP(5, ['платье1 5', 'сумка32 2', 'платье1 1', 'сумка23 2', 'сумка128 4']),
                     ['платье1 6', 'сумка128 4', 'сумка23 2', 'сумка32 2'])


def test_2_negative(self):
    self.assertEqual(ShopOLAP(8, ['123 5', '32 3', '124 5', '128 1', '32 2', '23 4', '128 4', '128 1']),
                     ['128 6', '123 5', '124 5', '32 5', '23 4'])
// для тестирования используется значения переменных, которые нужно менять на лету


2.
def __init__(self):
    self.__SERVICE_ARRAY = [0, 1, 0, -1, 0, 1, 0]  # service array for capture cells

def ConquestCampaign(N: int, M: int, L: int, battalion: list) -> int:
    neighbor = self.__SERVICE_ARRAY

// используется константа при инициализации объекта класса, в которой записан массив,
// на основании которого производится отбор соседних ячеек (согласно задаче)
// константа может быть изменена при изменении логики отбора


3.
# module of encoding symbols
class EncodingSymbols:
    def __init__(self):
        self.REVERCE = ''.maketrans('1234567890', '++++++++++')
        self.AVERS = ''.maketrans('+', '1')

    def reverce:
        return self.REVERCE

    def avers:
        return self.AVERS

# main module
from EncodingSymbols import EncodingSymbols  # module of encoding symbols
def plus_to_years(tree: list, revert: bool) -> list:
    new_tree = []

    if revert:
        revert_table = EncodingSymbols.reverce()
    else:
        revert_table = EncodingSymbols.avers()

// в модуле EncodingSymbols хранится таблица подстановки
// в основной модуль импортируются константы
// логику подстановки всегда можно изменить в зависимости от данных модуля