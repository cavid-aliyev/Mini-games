# X and 0 in python

#Oyunun lovhesi
board = ['', '', '', '', '', '', '', '', '']

#Oyunun lovhesini qururuq
def print_state(state):
    for i, c in enumerate(state):
        if(i+1) % 3 == 0:
            print(f'{c}')
        else:
            print(f'{c}|', end='')

#Uduş kombinasiyalari
winning_combinations = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (2,5,8), (0,4,8), (2,4,6)]


#Udan oyuncunu mueyyen edirik
def get_winner(state, combinations):
    for (x,y,z) in combinations:
        if state[x] == state[y] and state[z] == state[x] and (state[x] == "X" or state[x] == 'O'):
            return state[x]
    return ''


#Oyuncular x ve 0'ı harda yazmaq istədiklərini yazıb boardda yerləşdirirlər
def play_game(board):
    current_sign = 'X'
    while(get_winner(board, winning_combinations) == ''):
        index = int(input(f'{current_sign} harda yazmaq istəyirsiniz?'))
        board[index] = current_sign

        print_state(board)
        winner_sign = get_winner(board, winning_combinations)
        if winner_sign != '':
            print(f'Bizim qalibimiz var: {winner_sign}!')

        current_sign = 'X' if current_sign == 'O' else 'O'


play_game(board)

