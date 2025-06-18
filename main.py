import random
import os
import sys
import time
import msvcrt  # Windows 전용

WIDTH, HEIGHT = 20, 10
EMPTY = ' '
SNAKE_CHAR = 'O'
STAR_CHAR = '*'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(snake, star, score):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) == star:
                print(STAR_CHAR, end='')
            elif (x, y) in snake:
                print(SNAKE_CHAR, end='')
            else:
                print(EMPTY, end='')
        print()
    print(f"Score: {score}")
    print("Use WASD keys to move. Press 'Q' to quit.")

def get_key():
    if os.name == 'nt':
        if msvcrt.kbhit():
            key = msvcrt.getch()
            try:
                return key.decode('utf-8').lower()
            except:
                return ''
    return ''

def main():
    snake = [(WIDTH // 2, HEIGHT // 2)]
    direction = (1, 0)
    star = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
    score = 0
    game_over = False

    while not game_over:
        clear_screen()
        print_board(snake, star, score)

        key = get_key()
        if key == 'w' and direction != (0, 1):
            direction = (0, -1)
        elif key == 's' and direction != (0, -1):
            direction = (0, 1)
        elif key == 'a' and direction != (1, 0):
            direction = (-1, 0)
        elif key == 'd' and direction != (-1, 0):
            direction = (1, 0)
        elif key == 'q':
            print("게임 종료!")
            sys.exit()

        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        # 충돌 체크
        if not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT) or new_head in snake:
            game_over = True
            break

        snake.insert(0, new_head)

        if new_head == star:
            score += 1
            while True:
                star = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
                if star not in snake:
                    break
        else:
            snake.pop()

        time.sleep(0.15)  # 조금 더 빠르게 조정

    clear_screen()
    print_board(snake, star, score)
    print("게임 오버! 점수:", score)

if __name__ == "__main__":
    main()
