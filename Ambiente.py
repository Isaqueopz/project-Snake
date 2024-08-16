import random
import os
import time
import threading

# Dimensões do tabuleiro
ROWS = 40
COLS = 40

# Direções
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Variáveis globais
direction = RIGHT
direction_lock = threading.Lock()
running = True

def clear_screen():
    # Limpar tela dependendo do sistema operacional
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_segment(board, x, y, horizontal):
    if horizontal:
        board[y][x] = '='
    else:
        board[y][x] = '║'

def print_board(snake, food):
    clear_screen()  # Limpar a tela
    board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]

    # Desenhar a cobra
    for i in range(len(snake)):
        x, y = snake[i]
        if i > 0:
            prev_x, prev_y = snake[i - 1]
            horizontal = (y == prev_y)
            draw_segment(board, x, y, horizontal)
        else:
            board[y][x] = 'O'  # Cabeça da cobra

    # Desenhar o alimento
    fx, fy = food
    if 0 <= fx < COLS and 0 <= fy < ROWS:
        board[fy][fx] = 'O'

    # Exibir o tabuleiro
    for row in board:
        print(''.join(row))
    print()

def move_snake(snake, direction):
    head = snake[0]
    new_head = (head[0] + direction[0], head[1] + direction[1])
    return [new_head] + snake[:-1]

def change_direction():
    global direction
    global running

    while running:
        command = input("Use 'w' para cima, 's' para baixo, 'a' para esquerda, 'd' para direita (ou 'q' para sair): ")
        
        with direction_lock:
            if command == 'q':
                running = False
                break
            elif command == 'w':
                if direction != DOWN:
                    direction = UP
            elif command == 's':
                if direction != UP:
                    direction = DOWN
            elif command == 'a':
                if direction != RIGHT:
                    direction = LEFT
            elif command == 'd':
                if direction != LEFT:
                    direction = RIGHT

def main():
    global running
    snake = [(5, 5), (5, 4), (5, 3)]

    # Colocar alimento
    food = (random.randint(0, COLS-1), random.randint(0, ROWS-1))

    # Iniciar thread para mudar a direção
    direction_thread = threading.Thread(target=change_direction)
    direction_thread.start()
    
    while running:
        print_board(snake, food)
        
        # Mover a cobra
        snake = move_snake(snake, direction)

        # Verificar se a cobra comeu o alimento
        if snake[0] == food:
            snake.append(snake[-1])  # Adicionar segmento à cobra
            food = (random.randint(0, COLS-1), random.randint(0, ROWS-1))  # Novo alimento
        
        # Verificar se a cobra bateu nas paredes ou em si mesma
        head = snake[0]
        if not (0 <= head[0] < COLS and 0 <= head[1] < ROWS) or head in snake[1:]:
            print("Game Over!")
            running = False
        
        time.sleep(0.2)  # Ajustar a velocidade do jogo
    
    direction_thread.join()

if __name__ == "__main__":
    main()
