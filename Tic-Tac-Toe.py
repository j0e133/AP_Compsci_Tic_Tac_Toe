import random


BOARD = '''
    1   2   3
  +---+---+---+
1 | {} | {} | {} | 1
  +---+---+---+
2 | {} | {} | {} | 2
  +---+---+---+
3 | {} | {} | {} | 3
  +---+---+---+
    1   2   3
'''
SCORE = '''
Score:
X: {}
O: {}
'''
WINS = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8))
VALID_INPUT = ('1', '2', '3')


def get_win(board: list[str]) -> str:
    for i, j, k in WINS:
        if board[i] == board[j] == board[k] != ' ':
            print(board[i], ' won')
            return board[i]

    for spot in board:
        if spot == ' ':
            return 'Undecided'

    return 'Tie'


def play_game() -> str:
    board = [' ' for i in range(9)]

    turn = random.choice(['X', 'O'])

    winner = 'Undecided'

    print(BOARD.format(*board))
    print(turn, '\'s turn')

    while winner == 'Undecided':
        while True:
            dx = input('X: ')

            if dx in VALID_INPUT:
                x = int(dx) - 1
                break
            else:
                print('Invalid X!')

        while True:
            dy = input('Y: ')

            if dy in VALID_INPUT:
                y = int(dy) - 1
                break
            else:
                print('Invalid Y!')

        index = y * 3 + x

        if board[index] == ' ':
            if turn == 'X':
                board[index] = 'X'
            elif turn == 'O':
                board[index] = 'O'

            winner = get_win(board)

            if turn == 'X':
                turn =  'O'
            elif turn == 'O':
                turn = 'X'

            print(BOARD.format(*board))
            print(turn, '\'s turn')


        else:
            print('Spot already taken!')

    print()

    if winner == 'Tie':
        print('Tie!')
    else:
        print(winner + ' Won!')

    return winner


if __name__ == '__main__':
    x = 0
    o = 0
    tie = 0
    play_again = 'yes'

    while play_again == 'yes':
        winner = play_game()

        if winner == 'X':
            x += 1
        elif winner == 'O':
            o += 1
        else:
            tie += 1

        print(SCORE.format(x + tie * 0.5, o + tie * 0.5))

        play_again = input('Play again? ')

    print()
    print('Thanks for playing Tic-Tac-Toe!')
    print()

