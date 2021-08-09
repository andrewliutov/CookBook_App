cook_book = {}

with open('recipes.txt', 'r', encoding='utf8') as file:
    for line in file:
        dish_name = line.strip()
        cook_book.setdefault(dish_name, [])
        ingredients_qty = int(file.readline().strip())
        for item in range(ingredients_qty):
            ingredient_line = file.readline().strip().split(' | ')
            cook_book[dish_name] += [{'ingredient_name': ingredient_line[0],
                'quantity': ingredient_line[1], 'measure': ingredient_line[2]}]
        file.readline()


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingr_line in cook_book[dish]:
            if ingr_line['ingredient_name'] in shop_list.keys():
                shop_list[ingr_line['ingredient_name']]['quantity'] += \
                    int(ingr_line['quantity']) * person_count
            else:
                shop_list[ingr_line['ingredient_name']] = {
                    'quantity': int(ingr_line['quantity']) * person_count,
                    'measure': ingr_line['measure']}
    return shop_list
