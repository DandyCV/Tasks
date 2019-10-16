pizza_list = [["кукурудза", "томат", "гриби"], ["томат", "кукурудза", "гриби"],
              ["каперси", "курка", "томат"], ["гриби", "кукурудза", "томат"],
              ["каперси", "шинка", "томат"]]


def popular_pizza(p_list):
    '''Вивести найбільш популярну піцу з масиву'''

    pizza_menu = {}
    for pizza in p_list:
        new_pizza = frozenset(pizza)
        if new_pizza in pizza_menu.keys():
            pizza_menu[new_pizza] += 1
        else:
            pizza_menu.update({new_pizza: 1})
    best_pizza = max(pizza_menu.items(), key=lambda x: x[1])
    print(list(best_pizza[0]), " = ", best_pizza[1])


popular_pizza(pizza_list)