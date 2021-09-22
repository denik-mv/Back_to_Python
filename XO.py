def print_field():
    for coord in field:
        print(f'|{field[coord]}', end='')
        if coord % 10 == 3:
            print('|')


def win(field, xo, player):
    win_situation = False
    for z in [10, 20, 30]:
        if field[z+1] == field[z+2] == field[z+3] == xo:
            win_situation = True
    for z in [1, 2, 3]:
        if field[z+10] == field[z+20] == field[z+30] == xo:
            win_situation = True
    if field[11] == field[22] == field[33] == xo:
        win_situation = True
    if field[13] == field[22] == field[31] == xo:
        win_situation = True
    if win_situation:
        print(f'Игрок {player} победил!')
        return False
    return True


field = {
    11: ' ', 12: ' ', 13: ' ',
    21: ' ', 22: ' ', 23: ' ',
    31: ' ', 32: ' ', 33: ' ',
}
empty_space = [11, 21, 31, 12, 22, 32, 13, 23, 33]
turn, xo, player = 1, '_', 1
print_field()
while win(field, xo, player):
    if turn % 2 == 0:
        player, xo = 2, 'o'
    else:
        player, xo = 1, 'x'
    try:
        coord = int(input(f'Введите координати (yx) для {xo} игрок {player}: '))
    except ValueError:
        print('Введенные координаты некоректные либо поле уже использованно.')
        print_field()
        continue
    if coord in empty_space:
        field[coord] = xo
        turn += 1
        empty_space.remove(int(coord))
    else:
        print('Введенные координаты некоректные либо поле уже использованно.')
    if not empty_space:
        print('Игра завершилась ничьей.')
        print_field()
        break
    print_field()
