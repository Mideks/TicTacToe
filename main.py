def print_field(field):
    lines = []
    for row in field:
        lines.append(" " + " | ".join(row) + " ")
    print("\n — + — + — \n".join(lines))


def get_player_move():
    # todo: добавить обработку ошибок
    row = int(input("Введите строку (0, 1 или 2): "))
    col = int(input("Введите столбик (0, 1 или 2): "))
    return row, col


def update_field(field, row, col, player_symbol):
    if field[row][col] == " ":
        field[row][col] = player_symbol
        return True
    else:
        print("Клетка уже занята. Попробуй снова\n")
        return False


def check_win(field, current_player):
    return False


def check_draw(field):
    return False


def tick_tac_toe():
    field = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    current_player = "X"

    while True:
        print_field(field)
        print(f"Ход игрока {current_player}")

        row, col = get_player_move()
        if update_field(field, row, col, current_player):
            if check_win(field, current_player):
                print_field(field)
                print(f"Игрок {current_player} победил")
                break

            if check_draw(field):
                print_field(field)
                print(f"Ничья!")
                break

            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"


tick_tac_toe()