import random
import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

FPS = pygame.time.Clock()

COLOR_WHITE = (225, 225, 225)
COLOR_BLACK = (0, 0 , 0)
COLOR_BLUE = (0, 0, 255)
COLOR_YELLOW = (255, 255, 204)

player_size = (20, 20)

HEIGHT = 1200
WIDTH = 800

main_display = pygame.display.set_mode((HEIGHT, WIDTH))

player = pygame.Surface(player_size)
player.fill(COLOR_WHITE)
player_rect = player.get_rect()
# player_speed = [1, 1]
player_move_down = [0, 1]
player_move_right = [1, 0]
player_move_left = [-1, 0]
player_move_up = [0, -1]

def create_enemy():
    enemy_size = (30, 30)
    enemy = pygame.Surface(enemy_size) 
    enemy.fill(COLOR_BLUE)
    enemy_rect = pygame.Rect(HEIGHT, random.randint(0, WIDTH), *enemy_size)
    enemy_move = [random.randint(-6, -1), 0]
    return [enemy, enemy_rect, enemy_move]

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

playing = True

enemies = []

while playing:
    FPS.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy()) 

    main_display.fill(COLOR_BLACK)

    keys = pygame.key.get_pressed()

    if keys[K_DOWN] and player_rect.bottom < WIDTH:
        player_rect = player_rect.move(player_move_down)

    if keys[K_RIGHT] and player_rect.right<HEIGHT:
        player_rect = player_rect.move(player_move_right)

    if keys[K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move(player_move_left)

    if keys[K_UP] and player_rect.top > 0:
        player_rect = player_rect.move(player_move_up)

    for enemy in enemies: 
        enemy[1] = enemy[1].move(enemy[2])
        main_display.blit(enemy[0], enemy[1])
        if player_rect.colliderect(enemy[1]):
            playing = False
        

    # enemy_rect = enemy_rect.move(enemy_move)

    # if player_rect.bottom >= WIDTH:
    #     player_speed = random.choice(([1, -1], [-1, -1]))

    # if player_rect.top <= 0:
    #     player_speed = random.choice(([-1, 1], [1, 1]))

    # if player_rect.right >= HEIGHT:
    #     player_speed = random.choice(([-1,  -1], [-1, 1]))

    # if player_rect.left <= 0:
    #     player_speed = random.choice(([1, 1], [1, -1]))

    main_display.blit(player, player_rect)
    
    # main_display.blit(enemy, enemy_rect)

    # player_rect=player_rect.move(player_speed)

    pygame.display.flip()

    for enemy in enemies:
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))
