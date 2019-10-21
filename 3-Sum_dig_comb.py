import itertools

total_sum1 = 4
digits1 = [1, 2, 3]

total_sum2 = 10
digits2 = [2, 5, 3, 6]


def sum_digits_combination(digits_sum, digits_list):
    """Задано сума і список чисел, з яких потрібно скласти таку комбінаціяю,
    яка б дорівнювала вказаній сумі."""
    combinations = 0
    combinations_list = []
    for L in range(1, digits_sum//min(digits_list)+1):
        for subset in itertools.combinations_with_replacement(digits_list, L):
           if sum(subset) == digits_sum:
                combinations_list.append(subset)
                combinations += 1
    print(sorted(combinations_list))
    print(combinations)


sum_digits_combination(total_sum1, digits1)