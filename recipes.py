a = ['ingredient_name', 'quantity', 'measure']
cook_book = {}
rec = open('rec.txt', 'w', encoding='utf-8')
with open('recipes.txt', 'r', encoding='utf-8') as menu:
    for line in menu:
        recipe = line.strip()
        count_ingedients = menu.readline()
        cook_book[recipe] = []
        key_ = []
        for i in range(int(count_ingedients)):
            q = menu.readline().strip().split(' | ')
            a = dict(zip(a, q))
            cook_book[recipe].append(a)
        menu.readline()


def get_shop_list_by_dishes(dishes, person_count):
    out = {}
    ingr_list = []
    for dish in dishes:
        ingr_list = cook_book[dish]
        for i in ingr_list:
            ingredient_name = i['ingredient_name']
            if out.get(ingredient_name) is None:
                out[ingredient_name] = {'measure': i['measure'], 'quantity': int(i['quantity']) * person_count}
            else:
                out[ingredient_name]['quantity'] += int(i['quantity']) * person_count
    #        print(ingr_list)
    print(out)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

