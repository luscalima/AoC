import re

def _to_int(pairs):
    return [tuple([int(i) for i in pair]) for pair in pairs]

def get_pairs(id):
    return _to_int(re.findall('(\d*)-(\d*)', id))

def is_contained(first, second):
    first_set = set(range(first[0], first[1]+1))
    second_set = set(range(second[0], second[1]+1))

    return bool(len(first_set & second_set))

with open('input.txt') as f:
    ids_pairs = f.readlines()
    contained_count = 0

    for id in ids_pairs:
        first_pair, second_pair = get_pairs(id.strip())
        contained = is_contained(first_pair, second_pair)
        
        if contained:
            contained_count += 1

    print(contained_count)