# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()


# Window
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "Stealing For the Band"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Variables

num_keys = 0

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MANN_BLUE = (80, 163, 217)

# Images
auditorium = pygame.image.load('stage.jpg')
door = pygame.image.load('door.png')
gym = pygame.image.load('gym.jpg')
stairs = pygame.image.load('stairs.jpg')
stairs_rotated = pygame.image.load('stairs_rotated.jpg')
key_img = pygame.image.load('key.png')
coin_img = pygame.image.load('coin.png')
key_score = pygame.image.load('key_score.png')
coin_score = pygame.image.load('coin_score.png')

def draw_background(x, y):
    screen.blit(auditorium, (x+200, y+360))
    screen.blit(gym, (x+480, y+360))
    
    screen.blit(door, (x+180, y+360))
    screen.blit(door, (x+180, y+420))
    screen.blit(door, (x+320, y+360))
    screen.blit(door, (x+320, y+420))
    screen.blit(door, (x+460, y+360))
    screen.blit(door, (x+460, y+420))
    screen.blit(door, (x+640, y+360))
    screen.blit(door, (x+640, y+420))
    screen.blit(door, (x+100, y+520))
    screen.blit(door, (x+680, y+520))
    screen.blit(door, (x+700, y+400))
    screen.blit(door, (x+700, y+340))
    screen.blit(door, (x+160, y+60))
    screen.blit(door, (x+220, y+60))
    screen.blit(door, (x+600, y+60))
    screen.blit(door, (x+660, y+60))
    screen.blit(door, (x+280, y+280))
    
    screen.blit(stairs, (x+240, y+80))
    screen.blit(stairs, (x+640, y+80))
    screen.blit(stairs, (x+240, y+240))
    screen.blit(stairs, (x+580, y+240))
    screen.blit(stairs_rotated, (x+500, y+280))

def check_doors():
    global num_keys, doors

    locked_doors = []

    for d in doors:
        if intersects.rect_rect(player1, d):        
            if(d[4] == CLOSED and num_keys > 0):
                d[4] = OPEN
                num_keys -= 1
                print('unlocked')
        if d[4] == CLOSED:
            locked_doors.append(d)

    return locked_doors

def write_score():
    screen.blit(key_score, [10, 10])
    screen.blit(coin_score, [10, 70])
    
    font = pygame.font.Font(None, 80)
    text = font.render(str(num_keys), 1, GREEN)
    screen.blit(text, [70, 10])

    font = pygame.font.Font(None, 80)
    text = font.render(str(score1), 1, GREEN)
    screen.blit(text, [70, 70])
    
# Make a player
player1 =  [200, 150, 20, 20]
vel1 = [0, 0]
player1_speed = 2
score1 = 0

# Make a second player
player2 =  [500, 150, 20, 20]
vel2 = [0, 0]
player2_speed = 1
score2 = 0

# Door States
OPEN = True
CLOSED = False

# make doors
door1 = [180, 360, 20, 20, CLOSED]
door2 = [180, 420, 20, 20, CLOSED]
door3 = [320, 360, 20, 20, CLOSED]
door4 = [320, 420, 20, 20, CLOSED]
door5 = [460, 360, 20, 20, CLOSED]
door6 = [460, 420, 20, 20, CLOSED]
door7 = [640, 360, 20, 20, CLOSED]
door8 = [640, 420, 20, 20, CLOSED]
door9 = [100, 520, 20, 20, CLOSED]
door10 = [680, 520, 20, 20, CLOSED]
door11 = [700, 400, 20, 20, CLOSED]
door12 = [700, 340, 20, 20, CLOSED]
door13 = [160, 60, 20, 20, CLOSED]
door14 = [220, 60, 20, 20, CLOSED]
door15 = [600, 60, 20, 20, CLOSED]
door16 = [660, 60, 20, 20, CLOSED]
door17 = [280, 280, 20, 20, CLOSED]

doors = [door1, door2, door3, door4, door5, door6, door7, door8, door9, door10, door11, door12, door13, door14, door15, door16, door17]

# make walls
wall1 =  [0, 460, 80, 40]
wall2 =  [80, 460, 20, 80]
wall3 =  [0, 420, 60, 20]
wall4 =  [80, 340, 20, 100]
wall5 = [0, 340, 60, 20]
wall6 = [0, 280, 140, 40]
wall7 = [120, 340, 40, 120]
wall8 = [180, 440, 160, 20]
wall9 = [180, 380, 20, 40]
wall10 = [120, 480, 240, 20]
wall11 = [180, 340, 160, 20]
wall12 = [320, 380, 20, 40]
wall13 = [120, 500, 20, 40]
wall14 = [340, 500,  20, 40]
wall15 = [140, 60, 20, 260]
wall16 = [180, 240, 40, 60]
wall17 = [180, 100, 40, 120]
wall18 = [180, 60, 40, 20]
wall19 = [240, 60, 40, 20]
wall20 = [260, 80, 20, 200]
wall21 = [240, 120, 20, 120]
wall22 = [240, 280, 40, 20]
wall23 = [300, 260, 40, 40]
wall24 = [440, 480, 20, 60]
wall25 = [460, 480, 200, 20]
wall26 = [660, 480, 20, 60]
wall27 = [460, 440, 220, 20]
wall28 = [460, 380, 20, 40]
wall29 = [460, 340, 200, 20]
wall30 = [640, 380, 20, 40]
wall31 = [700, 440, 20, 100]
wall32 = [720, 440, 80, 60]
wall33 = [680, 340, 20, 80]
wall34 = [720, 340, 60, 20]
wall35 = [720, 400, 60, 20]
wall36 = [780, 340, 20, 80]
wall37 = [320, 220, 20, 40]
wall38 = [340, 220, 120, 20]
wall39 = [460, 220, 20, 80]
wall40 = [480, 260, 20, 40]
wall41 = [500, 260, 80, 20]
wall42 = [540, 280, 60, 20]
wall43 = [560, 220, 20, 40]
wall44 = [580, 60, 20, 180]
wall45 = [620, 240, 40, 60]
wall46 = [620, 140, 40, 80]
wall47 = [620, 60, 40, 20]
wall48 = [620, 80, 20, 40]
wall49 = [620, 120, 40, 20]
wall50 = [680, 60, 20, 240]
wall51 = [680, 300, 120, 20]

walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13, wall14, wall15, wall16, wall17, wall18, wall19, wall20, wall21, wall22, wall23, wall24, wall25, wall26, wall27, wall28, wall29, wall30, wall31, wall32, wall33, wall34, wall35, wall36, wall37, wall38, wall39, wall40, wall41, wall42, wall43, wall44, wall45, wall46, wall47, wall48, wall49, wall50, wall51]

# Make coins
coin1 = [300, 500, 25, 25]
coin2 = [400, 200, 25, 25]
coin3 = [150, 150, 25, 25]

coins = [coin1, coin2, coin3]

# Make keys
key1 = [450, 450, 20, 20]

keys = [key1]


# Game loop
win = False
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()

    player1_up = pressed[pygame.K_UP]
    player1_down = pressed[pygame.K_DOWN]
    player1_left = pressed[pygame.K_LEFT]
    player1_right = pressed[pygame.K_RIGHT]

    if player1_left:
        vel1[0] = -player1_speed
    elif player1_right:
        vel1[0] = player1_speed
    else:
        vel1[0] = 0

    if player1_up:
        vel1[1] = -player1_speed
    elif player1_down:
        vel1[1] = player1_speed
    else:
        vel1[1] = 0


    player2_up = pressed[pygame.K_w]
    player2_down = pressed[pygame.K_s]
    player2_left = pressed[pygame.K_a]
    player2_right = pressed[pygame.K_d]

    if player2_left:
        vel2[0] = -player2_speed
    elif player2_right:
        vel2[0] = player2_speed
    else:
        vel2[0] = 0

    if player2_up:
        vel2[1] = -player2_speed
    elif player2_down:
        vel2[1] = player2_speed
    else:
        vel2[1] = 0
        
        
    # Game logic (Check for collisions, update points, etc.)
    ''' move the player in horizontal direction '''
    player1[0] += vel1[0]

    ''' check doors '''
    locked = check_doors()

    ''' resolve collisions horizontally '''
    
    collidables = walls + locked
    
    for c in collidables:
        if intersects.rect_rect(player1, c):        
            if vel1[0] > 0:
                player1[0] = c[0] - player1[2]
            elif vel1[0] < 0:
                player1[0] = c[0] + c[2]

    ''' move the player in vertical direction '''
    player1[1] += vel1[1]

    ''' check doors '''
    locked = check_doors()
        
    ''' resolve collisions vertically '''
    collidables = walls + locked

    
    for c in collidables:
        if intersects.rect_rect(player1, c):                    
            if vel1[1] > 0:
                player1[1] = c[1] - player1[3]
            if vel1[1]< 0:
                player1[1] = c[1] + c[3]


    ''' here is where you should resolve player collisions with screen edges '''




    ''' get the coins '''   
    hit_list = [c for c in coins if intersects.rect_rect(player1, c)]
    
    for hit in hit_list:
        coins.remove(hit)
        score1 += 1
        print("sound!")
        
    if len(coins) == 0:
        win = True

    ''' get the keys '''
    keys_hit = [k for k in keys if intersects.rect_rect(player1, k)]
    
    for hit in keys_hit:
        keys.remove(hit)
        num_keys += 1
        print("sound!")

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    draw_background(0, 0)

    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, GREEN, player2)

    
    for w in walls:
        pygame.draw.rect(screen, MANN_BLUE, w)

    for c in coins:
        screen.blit(coin_img, c)

    for k in keys:
        screen.blit(key_img, k)
        
        
    if win:
        font = pygame.font.Font(None, 48)
        text = font.render("You Win!", 1, GREEN)
        screen.blit(text, [400, 200])

    write_score()

    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
