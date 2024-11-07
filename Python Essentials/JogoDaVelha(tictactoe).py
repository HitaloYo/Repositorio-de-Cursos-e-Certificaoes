from random import randrange

# Função para exibir o tabuleiro
def display_board(board):
    for row in board:
        print("+-------" * 3 + "+")
        print("|       " * 3 + "|")
        print("|   " + "   |   ".join(map(str, row)) + "   |")
        print("|       " * 3 + "|")
    print("+-------" * 3 + "+")

# Função para inserir o movimento do jogador
def enter_move(board):
    while True:
        try:
            move = int(input("Digite seu movimento: ")) - 1
            row, col = divmod(move, 3)
            if 0 <= move < 9 and str(board[row][col]).isdigit():
                board[row][col] = 'O'
                break
            else:
                print("Movimento inválido. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")

# Função para encontrar os campos livres
def make_list_of_free_fields(board):
    free_fields = []
    for r, row in enumerate(board):
        for c, cell in enumerate(row):
            if str(cell).isdigit():
                free_fields.append((r, c))
    return free_fields

# Função para verificar o vencedor
def victory_for(board, sign):
    win_patterns = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    for pattern in win_patterns:
        if all(board[r][c] == sign for r, c in pattern):
            return True
    return False

# Função para o movimento aleatório do computador
def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    row, col = free_fields[randrange(len(free_fields))]
    board[row][col] = 'X'

def tic_tac_toe():
    board = [
        [1, 2, 3],
        [4, 'X', 6],
        [7, 8, 9]
    ]
    while True:
        display_board(board)
        enter_move(board)
        if victory_for(board, 'O'):
            display_board(board)
            print("Você ganhou!")
            break
        if not make_list_of_free_fields(board):
            display_board(board)
            print("Empate!")
            break
        draw_move(board)
        if victory_for(board, 'X'):
            display_board(board)
            print("Você perdeu!")
            break
        if not make_list_of_free_fields(board):
            display_board(board)
            print("Empate!")
            break

tic_tac_toe()
