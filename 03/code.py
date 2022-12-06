def divide_items(items):
    middle = int(len(items) / 2)

    return [items[0:middle], items[middle:]]

def find_commom_item(items_parts):
    first_part, second_part = items_parts

    for item in first_part:
        if item in second_part:
            return item

def commom_item_points(commom_item):
    lower_shift = ord('a') - 1
    upper_shift = ord('A') - 27

    return ord(commom_item) - (lower_shift if commom_item.islower() else upper_shift)

def group_in(items, size):
    for index in range(0, len(items), size):
        yield items[index:index + size]

def find_badge(group):
    first, second, third = group
    badge = set(first.strip()) & set(second.strip()) & set(third.strip())
    return badge.pop()

with open('input.txt') as f:
    items = f.readlines()

    items_points_sum = 0

    # Início - Códiog da primeira parte
    # for line in items:
    #     items_parts = divide_items(line.strip())
    #     commom_item = find_commom_item(items_parts)
    #     item_points = commom_item_points(commom_item)
    #     items_points_sum += item_points
    # Fim

    # Início - Código da segunda parte
    for group in group_in(items, 3):
        badge = find_badge(group)
        item_points = commom_item_points(badge)
        items_points_sum += item_points
    # Fim

    print(items_points_sum)
