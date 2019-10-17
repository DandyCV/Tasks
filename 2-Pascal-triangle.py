def pascal_triangle(row_number):
    '''Визначити числа в заданому рядку трикутника Паскаля задопомогою рекурсії'''
    if row_number==1:
        return ([1])
    elif row_number==2:
        return ([1, 2, 1])
    else:
        row=[1]
        for x in range(row_number-1):
            row.append(pascal_triangle(row_number-1)[x] + pascal_triangle(row_number-1)[x+1])
        row.append(1)
        return (row)


print(pascal_triangle(4))