import pygame, random, sys, time

pygame.init()

screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption("SNAKE!")

def show():
    square_size = 40
    for x in range(0, 10):
        for y in range(0,7):
            # draw grid
            if display[y*10 + x] == 1:
                rectColor = (255,255,255)
            elif display[y*10 + x] == 0:
                rectColor = (0,0,0)

            rect = pygame.Rect(x * square_size, y * square_size, square_size, square_size)
            pygame.draw.rect(screen, rectColor, rect, 0)
            pygame.draw.rect(screen, (0,255,255), rect, 2)
    #pygame update screen
    pygame.display.flip()


#
# both lists in same table, display 0-70 snake pos element 100
# direction = D variable
# apple = A variable
#
#
#


display = [0]*70
snakePos = [35, 45]
direction = 0
apple = 22

def update():
    global display
    global direction
    global apple
    global snakePos

    if direction == 0:
        snakePos.insert(0, snakePos[0] - 10)
    elif direction == 1:
        snakePos.insert(0, snakePos[0] + 1)
    elif direction == 2:
        snakePos.insert(0, snakePos[0] + 10)
    elif direction == 3:
        snakePos.insert(0, snakePos[0] - 1)

    if snakePos[0] == apple:
        apple = random.randint(0,70)
    else:
        snakePos.pop()

    for i in range(0, len(display)):
        if i in snakePos or i == apple:
            display[i] = 1
        else:
            display[i] = 0
    show()

while True:
    #quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = direction - 1
            if event.key == pygame.K_RIGHT:
                direction = direction + 1

            if direction > 3:
                direction = 0
            if direction < 0:
                direction = 3

    update()
    time.sleep(1)
    