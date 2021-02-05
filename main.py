import pygame, random, sys, time

pygame.init()

screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption("SNAKE!")

def show(display):
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


A = 0 #Apple
B = 1 #On
C = 0 #Off
D = 0 #Direction
E = 0 #Snake Length
F = 45 #TEMP
G = 0 #TEMP
H = 0 #HEAD
I = 0 #ITERATOR
J = 0 #TEMP

array = [0]*200

array[100] = F
A = random.randint(0,69)


def up():
    global H
    global array
    H = array[100]
    shift_snake()
    H = H - 10
    array[100] = H
    return

def down():
    global H
    global array
    H = array[100]
    shift_snake()
    H = H + 10
    array[100] = H
    return

def left():
    global H
    global array
    H = array[100]
    shift_snake()
    H = H - 1
    array[100] = H
    return

def right():
    global H
    global array
    H = array[100]
    shift_snake()
    H = H + 1
    array[100] = H
    return

def shift_snake():
    global H
    global I
    global F
    global E
    global G
    global array
    get_snake_length()
    for I in range(99 + E, 99, -1):
        G = array[I]
        F = I + 1
        array[F] = G
    return

def get_snake_length():
    global I
    global F
    global E
    global array
    for I in range(100,170):
        F = array[I]
        if F == 0:
            E = I
            E = E - 100
            break
    return


def remove_last_snake():
    global C
    global E
    global array
    get_snake_length()
    array[99 + E] = C
    return

def clear_display():
    global array
    global I
    for I in range(0,70):
        array[I] = C



def update():
    global A
    global B
    global C
    global D
    global E
    global F
    global G
    global H
    global I
    global J
    global array

    if D == 0:
        up()
    elif D == 1:
        right()
    elif D == 2:
        down()
    elif D == 3:
        left()

    H = array[100]
    if H == A:
        A = random.randint(1,70)
    else:
        remove_last_snake()

    #move snake position to display
    get_snake_length()
    clear_display()
    for I in range(E):
        F = array[I + 100]
        G = F-1
        array[G] = B
    
    F = A - 1
    array[F] = B
    
    show(display = array[0:70])
    return

while True:
    #quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                D = D - 1
            if event.key == pygame.K_RIGHT:
                D = D + 1

            if D > 3:
                D = 0
            if D < 0:
                D = 3

    update()
    time.sleep(1)
    