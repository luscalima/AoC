import re

def get_intial_stacks_state(raw_lines):
    lines = []

    for line in raw_lines:
        if not line.strip():
            break
        lines.append(line)

    lines.reverse()
    stacks = list(map(lambda n: [int(n)], re.findall('\d', lines.pop(0))))

    for line in lines:
        for stack in stacks:
            crate_index = ((stack[0] - 1) * 4) + 1
            crate = line[crate_index]
            
            if crate.isspace():
                continue

            stack.append(crate)
    
    return stacks

def get_moves(lines):

    for line in lines:
        move = list(map(int, re.findall('(\d+)', line)))
        if len(move) != 3:
            continue
        yield move

def splice_stack(arr, amount):
    new_arr = []
    
    for i in range(amount):
        new_arr.append(arr.pop())

    new_arr.reverse()

    return new_arr

with open('input.txt') as f:
    lines = f.readlines()
    stacks = get_intial_stacks_state(lines)

    for move in get_moves(lines):
        # move from to
        m, f, t = move

        # Início - Código primeira parte
        # for i in range(m):
        #     stacks[t-1].append(stacks[f-1].pop())
        # Fim

        # Início - Código segunda parte
        stacks[t-1].extend(splice_stack(stacks[f-1], m))
        # Fim

    top_crates = ''

    for stack in stacks:
        top_crates += stack[-1]
    
    print(top_crates)