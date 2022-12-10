with open('input.txt') as f:
    lines = [list(line) for line in f.read().strip().split('\n')]

def scenic_score(i, j):
    s = [0, 0, 0, 0]

    for number in lines[i][j-1::-1]:
        s[0] += 1
        if number >= lines[i][j]: break
    for number in lines[i][j+1:]:
        s[1] += 1
        if number >= lines[i][j]: break
    for index in list(range(i))[::-1]:
        s[2] += 1
        if lines[index][j] >= lines[i][j]: break
    for index in range(i+1, len(lines)):
        s[3] += 1
        if lines[index][j] >= lines[i][j]: break
    
    return s[0] * s[1] * s[2] * s[3]

# Um conjunto, pois uma árvore em determinada coordenada não pode ser
# contabilizada mais de uma vez caso seja vista em mais de uma direção
visible_trees = set()

for i in range(1, len(lines) - 1):
    
    higher_ltr = lines[i][0]
    higher_rtl = lines[i][-1]
    higher_ttb = lines[0][i]
    higher_btt = lines[-1][i]

    for j in range(1, len(lines[i]) - 1):
    
        number_ltr = lines[i][j]
        number_rtl = lines[i][len(lines[i]) - j - 1] # Indexação inversa
        number_ttb = lines[j][i]
        number_btt = lines[len(lines[i]) - j - 1][i] # Indexação inversa

        # Esquerda > direita
        if number_ltr > higher_ltr:
            visible_trees.add((i, j))
            higher_ltr = number_ltr

        # Direita > esquerda
        if number_rtl > higher_rtl:
            visible_trees.add((i, len(lines[i]) - j - 1))
            higher_rtl = number_rtl
    
        # Cima > baixo
        if number_ttb > higher_ttb:
            visible_trees.add((j, i))
            higher_ttb = number_ttb

        # Baixo > cima
        if number_btt > higher_btt:
            visible_trees.add((len(lines[i]) - j - 1, i))
            higher_btt = number_btt

already_visible = len(lines) * 4 - 4
visible_count = len(visible_trees) + already_visible
higher_scenic_score = max([scenic_score(i, j) for i, j in visible_trees])

print(visible_count)
print(higher_scenic_score)