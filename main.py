import random

X_SYMBOL = "X"
O_SYMBOL = "O"
EMPTY = " "


def print_field(field):
    lines = []
    for row in field:
        lines.append(" " + " | ".join(row) + " ")
    print("\n — + — + — \n".join(lines))


def get_player_move():
    # todo: добавить обработку ошибок
    row = int(input("Введите строку (1, 2 или 3): ")) - 1
    col = int(input("Введите столбик (1, 2 или 3): ")) - 1
    return row, col


def get_bot_move():
    row = random.randint(1, 3) - 1
    col = random.randint(1, 3) - 1
    print(f"Бот сходил на клетку ({row}, {col}")
    return row, col


def update_field(field, row, col, player_symbol):
    if field[row][col] == EMPTY:
        field[row][col] = player_symbol
        return True
    else:
        print("Клетка уже занята. Попробуй снова\n")
        return False


def check_win(field, current_player):
    # проверяем победу в одной из строчек или в одном из столбцов
    for i in range(3):
        if all(field[i][j] == current_player for j in range(3)) or \
           all(field[j][i] == current_player for j in range(3)):
            return True

    # проверяем победу в диагоналях
    if all(field[i][i] == current_player for i in range(3)) or \
       all(field[i][2 - i] == current_player for i in range(3)):
        return True

    return False


def check_draw(field):
    if all(all(field[i][j] != EMPTY for i in range(3)) for j in range(3)):
        return True

    return False


def tick_tac_toe():
    field = [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]
    current_player = X_SYMBOL

    while True:
        print_field(field)
        print(f"Ход игрока {current_player}")

        if current_player == X_SYMBOL:
            row, col = get_player_move()
        else:
            row, col = get_bot_move()

        if update_field(field, row, col, current_player):
            if check_win(field, current_player):
                print_field(field)
                print(f"Игрок {current_player} победил")
                break

            if check_draw(field):
                print_field(field)
                print(f"Ничья!")
                break

            if current_player == X_SYMBOL:
                current_player = O_SYMBOL
            else:
                current_player = X_SYMBOL


tick_tac_toe()
