1.
def Football(f: list, n: int) -> bool:
    if f:
        k: list = []
        m: list = []
        f_up: list = f.copy()
        f_up.sort()

        for i in range(n):
            if f[i] != f_up[i] and f[i] > f[i + (1 if i < n-1 else 0)]:
                k.append(i)
                m.append(1)
            elif f[i] != f_up[i]:
                k.append(i)
                m.append(0)
            else:
                m.append(0)

// в данном случае отлично подойдет упорядоченный массив

2.
def white_walkers(village: str) -> bool:
    ind = []

    for i in range(len(village)):
        if '1' <= village[i] <= '9':
            ind.append(i)
    if len(ind) < 2:
        return False

    for i in range(len(ind) - 1):
        if int(village[ind[i]]) + int(village[ind[i + 1]]) == 10 and village[ind[i]:ind[i + 1] + 1].count('=') != 3:
            return False
    return True
// также можно применить упорядоченный массив

3.
def BiggerGreater(input_str: str) -> str:
    input_list = list(input_str)
    for i in range(len(input_list) - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if input_list[i] > input_list[j]:
                input_list[i], input_list[j] = input_list[j], input_list[i]
                return ''.join(rotate(j + 1, input_list))
    return ""

def rotate(i: int, input_list: list) -> list:
    for j in range(i, len(input_list)):
        for k in range(j + 1, len(input_list)):
            if input_list[k] < input_list[j]:
                input_list[k], input_list[j] = input_list[j], input_list[k]
    return input_list
// в этом случае целесообразно использовать два стека для составления упорядоченного списка
