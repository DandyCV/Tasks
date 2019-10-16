def pascal_triangle(row_number, prefix=[1]):
    '''Визначити числа в заданому рядку трикутника Паскаля задопомогою рекурсії'''
    if row_number == 1:
        print(prefix)
    else:
        new_prefix = [1]
        if len(prefix) == 1:
            prefix.append(1)
        for x in range(len(prefix)-1):
            new_prefix.append(prefix[x]+prefix[x+1])
        new_prefix.append(1)
        pascal_triangle(row_number-1, prefix=new_prefix)


pascal_triangle(6)