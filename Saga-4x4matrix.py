matrix_1 = [[7,0,7,0],
            [5,4,0,2],
            [1,9,4,2],
            [9,5,7,0]]

def find_3_repits(matrix):
    '''Шукає повтори з трьох одинакових елементів підряд
    в колонках, рядках чи діагоналях матриці 4х4'''

    #rows_search
    for row in matrix:
        if len(set(row[:3]))==1 or len(set(row[1:]))==1:
            return True
    #colums_search
    for index in range(4):
        colums_list = []
        for row in matrix:
            colums_list.append(row[index])
        if len(set(colums_list[:3])) == 1 or len(set(colums_list[1:])) == 1:
            return True
    #diagonals_search:
    diagonals_list = []
    for index in range(4):
        diagonals_list.append(matrix[index][index])
    if len(set(diagonals_list[:3])) == 1 or len(set(diagonals_list[1:])) == 1:
            return True
    diagonals_list.clear()
    for index in range(3, 0, -1):
        diagonals_list.append(matrix[index][3-index])
    if len(set(diagonals_list[:3])) == 1 or len(set(diagonals_list[1:])) == 1:
            return True

    return False


print(find_3_repits(matrix_1))