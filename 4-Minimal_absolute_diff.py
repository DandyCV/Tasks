def minimal_absolute_difference(n_list):
    '''Задано масив цілих чисел. Знайти мінімальну абсолютну різницю між елементами масиву'''
    diff = float('+inf')
    for x in range(len(n_list)):
        for y in range(x+1, len(n_list)):
            cur_diff = abs(n_list[x] - n_list[y])
            if cur_diff < diff:
                diff = cur_diff
    print(diff)


a = [3, -7, 0]

minimal_absolute_difference(a)