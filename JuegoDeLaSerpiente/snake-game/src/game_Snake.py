import curses
import random

# Inicializar la pantalla
screen = curses.initscr()
curses.curs_set(0)
sh, sw = screen.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

# Configuración inicial de la serpiente
snake_x = sw // 4
snake_y = sh // 2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]
]

# Configuración inicial de la comida
food = [sh // 2, sw // 2]
w.addch(food[0], food[1], curses.ACS_PI)

# Configuración inicial de la dirección
key = curses.KEY_RIGHT

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    # Calcular la nueva posición de la cabeza de la serpiente
    if key == curses.KEY_DOWN:
        new_head = [snake[0][0] + 1, snake[0][1]]
    elif key == curses.KEY_UP:
        new_head = [snake[0][0] - 1, snake[0][1]]
    elif key == curses.KEY_LEFT:
        new_head = [snake[0][0], snake[0][1] - 1]
    elif key == curses.KEY_RIGHT:
        new_head = [snake[0][0], snake[0][1] + 1]
    else:
        new_head = snake[0]

    # Insertar la nueva cabeza de la serpiente
    snake.insert(0, new_head)

    # Verificar si la serpiente ha comido la comida
    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh - 1),
                random.randint(1, sw - 1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    # Verificar colisiones
    if (snake[0][0] in [0, sh] or
        snake[0][1] in [0, sw] or
        snake[0] in snake[1:]):
        curses.endwin()
        quit()

    # Dibujar la serpiente
    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)