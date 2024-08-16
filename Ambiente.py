import random
import os
import time

# Dimensões do tabuleiro
ROWS = 34
COLS = 22

# Matriz do tabuleiro
matrix = [[0] * COLS for _ in range(ROWS)]

# Direções
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def print_board(snake, food):
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpar tela
    board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]

    # Desenhar a cobra
    for segment in snake:
        x, y = segment
        if 0 <= x < COLS and 0 <= y < ROWS:
            board[y][x] = '*'

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
    snake = [new_head] + snake[:-1]
    return snake

def main():
    snake = [(5, 5), (5, 4), (5, 3)]
    direction = RIGHT

    # Colocar alimento
    food = (random.randint(0, COLS-1), random.randint(0, ROWS-1))
    
    while True:
        print_board(snake, food)
        command = input("Use 'w' for up, 's' for down, 'a' for left, 'd' for right (or 'q' to quit): ")
        
        if command == 'q':
            break
        elif command == 'w':
            direction = UP
        elif command == 's':
            direction = DOWN
        elif command == 'a':
            direction = LEFT
        elif command == 'd':
            direction = RIGHT

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
            break
        
        time.sleep(0.2)  # Ajustar a velocidade do jogo

if __name__ == "__main__":
    main()

