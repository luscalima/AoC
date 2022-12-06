move_map = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}

i_must_map = {
    'X': 'loss',
    'Y': 'draw',
    'Z': 'win'
}

winner_move = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}

losser_move = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}

def move_score(move):
    return {
        'rock': 1,
        'paper': 2,
        'scissors': 3
    }.get(move)

def plus_score(round_result):
    return {
        'win': 6,
        'draw': 3,
        'loss': 0
    }.get(round_result)

def round_result(opponent_move, me_move):
    opponent = move_map.get(opponent_move)
    me = move_map.get(me_move)

    if me == opponent:
        return 'draw'
    elif (me, opponent) == ('rock', 'scissors') or (me, opponent) == ('scissors', 'paper') or (me, opponent) == ('paper', 'rock'):
        return 'win'
    elif (opponent, me) == ('rock', 'scissors') or (opponent, me) == ('scissors', 'paper') or (opponent, me) == ('paper', 'rock'):
        return 'loss'

with open('input.txt') as f:
    rounds = f.readlines()
    me_score = 0

    for round in rounds:
        opponent, me = round.strip().split(' ')

        # Início - Código da segunda parte
        i_must = i_must_map.get(me)

        if i_must == 'draw':
            me = opponent
        elif i_must == 'win':
            me = losser_move.get(opponent)
        else:
            me = winner_move.get(opponent)
        # Fim

        result = round_result(opponent, me)
        me_score += move_score(move_map.get(me)) + plus_score(result)
    
    print(me_score)