def x_wins():
    print('X wins')


def o_wins():
    print('O wins')


def draw():
    print('Draw')


def change_player():
    global symbol
    if symbol == 'X':
        symbol = 'O'
    elif symbol == 'O':
        symbol = 'X'


def impossible():
    print('Impossible')


def check_table(row_1, row_2, row_3):
    if row_1[0] == row_1[1] == row_1[2]:
        if row_1[0] != ' ' and row_1[0] != '_':
            same_in_a_row.append(row_1[0])

    if row_2[0] == row_2[1] == row_2[2]:
        if row_2[0] != ' ' and row_2[0] != '_':
            same_in_a_row.append(row_2[0])

    if row_3[0] == row_3[1] == row_3[2]:
        if row_3[0] != ' ' and row_3[0] != '_':
            same_in_a_row.append(row_3[0])

    if row_1[0] == row_2[0] == row_3[0]:
        if row_1[0] != ' ' and row_1[0] != '_':
            same_in_a_row.append(row_1[0])

    if row_1[1] == row_2[1] == row_3[1]:
        if row_1[1] != ' ' and row_1[1] != '_':
            same_in_a_row.append(row_1[1])

    if row_1[2] == row_2[2] == row_3[2]:
        if row_1[2] != ' ' and row_1[2] != '_':
            same_in_a_row.append(row_1[2])

    if row_1[0] == row_2[1] == row_3[2]:
        if row_1[0] != ' ' and row_1[0] != '_':
            same_in_a_row.append(row_1[0])

    if row_1[2] == row_2[1] == row_3[0]:
        if row_1[2] != ' ' and row_1[2] != '_':
            same_in_a_row.append(row_1[2])


def update_move(table, cell, row):
    if table[int(row) - 1][int(cell) - 1] == '_' or table[int(row) - 1][int(cell) - 1] == ' ':
        table[int(row) - 1][int(cell) - 1] = symbol


row_3 = [' ', ' ', ' ']
row_2 = [' ', ' ', ' ']
row_1 = [' ', ' ', ' ']
table = [row_1, row_2, row_3]

symbol = 'X'

while True:
    same_in_a_row = []

    print("---------")
    print(f"| {row_3[0]} {row_3[1]} {row_3[2]} |")
    print(f"| {row_2[0]} {row_2[1]} {row_2[2]} |")
    print(f"| {row_1[0]} {row_1[1]} {row_1[2]} |")
    print("---------")

    move = input('Enter the coordinates: ')
    coord_raw = move.split()
    coord = coord_raw[:2]
    if not coord[0].isnumeric():
        print('You should enter numbers!')
        continue
    elif int(coord[0]) not in range(1, 4) or int(coord[1]) not in range(1, 4):
        print('Coordinates should be from 1 to 3!')
        continue
    elif table[int(coord[1]) - 1][int(coord[0]) - 1] == 'X' or table[int(coord[1]) - 1][int(coord[0]) - 1] == 'O':
        print('This cell is occupied! Choose another one!')
        continue

    update_move(table, coord[0], coord[1])
    check_table(row_1, row_2, row_3)
    change_player()

    if len(same_in_a_row) == 1:
        print("---------")
        print(f"| {row_3[0]} {row_3[1]} {row_3[2]} |")
        print(f"| {row_2[0]} {row_2[1]} {row_2[2]} |")
        print(f"| {row_1[0]} {row_1[1]} {row_1[2]} |")
        print("---------")
        print(f'{same_in_a_row[0]} wins')
        break
    elif ' ' not in row_1 and ' ' not in row_2 and ' ' not in row_3:
        print("---------")
        print(f"| {row_3[0]} {row_3[1]} {row_3[2]} |")
        print(f"| {row_2[0]} {row_2[1]} {row_2[2]} |")
        print(f"| {row_1[0]} {row_1[1]} {row_1[2]} |")
        print("---------")
        draw()
        break