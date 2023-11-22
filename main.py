import random
import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

FPS = pygame.time.Clock()

COLOR_WHITE = (225, 225, 225)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_YELLOW = (255, 255, 204)

player_size = (20, 20)

HEIGHT = 1200
WIDTH = 800

main_display = pygame.display.set_mode((HEIGHT, WIDTH))

player = pygame.Surface(player_size)
player.fill(COLOR_WHITE)
player_rect = player.get_rect()

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

def create_bonus():
    bonus_size = (20, 20)
    bonus = pygame.Surface(bonus_size)
    bonus.fill(COLOR_YELLOW)
    bonus_rect = pygame.Rect(random.randint(0, HEIGHT), 0, *bonus_size)
    bonus_move = [0, random.randint(1, 6)]
    return [bonus, bonus_rect, bonus_move]

CREATE_ENEMY = pygame.USEREVENT + 1
CREATE_BONUS = pygame.USEREVENT + 2

pygame.time.set_timer(CREATE_ENEMY, 1500)
pygame.time.set_timer(CREATE_BONUS, 2000)

playing = True

enemies = []
bonuses = []

while playing:
    FPS.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())

    main_display.fill(COLOR_BLACK)

    keys = pygame.key.get_pressed()

    if keys[K_DOWN] and player_rect.bottom < WIDTH:
        player_rect = player_rect.move(player_move_down)

    if keys[K_RIGHT] and player_rect.right < HEIGHT:
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

    for bonus in bonuses:
        bonus[1] = bonus[1].move(bonus[2])
        main_display.blit(bonus[0], bonus[1])
        if player_rect.colliderect(bonus[1]):
            # Implement bonus effect here (e.g., increase player's score)
            bonuses.remove(bonus)

    main_display.blit(player, player_rect)
    
    pygame.display.flip()

    for enemy in enemies:
        if enemy[1].left < 0:
            enemies.remove(enemy)

    for bonus in bonuses:
        if bonus[1].top > WIDTH:
            bonuses.remove(bonus)
