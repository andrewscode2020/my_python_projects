'''SPACE INVADERS GAME USING PYGAME'''

import pygame
import random
import math
from pygame import mixer

# Initialize the pygame:
pygame.init()

# Create the screen:
screen = pygame.display.set_mode((800, 600))

# Background:
background = pygame.image.load('space_background.jpg')

# Background sound:
mixer.music.load('background.wav')
mixer.music.play(-1)  # Negative one is used to replay the song over and over again.

# Title and Icon:
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player:
playerImg = pygame.image.load('spaceship.png')
playerX = 368
playerY = 480
playerX_change = 0

# Enemies:
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('space_invader.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 100))
    enemyX_change.append(1)
    enemyY_change.append(30)

# Bullet:
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 4
bullet_state = 'ready'  # ready -> You can't see the bullet on the screen. fire -> Bullet moving.

# Score:
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game Over Text:
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render('Score: ' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text(): # We don't need to add (x, y) because it's always going to show in the same place.
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

# Player function:
def player(x, y):
    screen.blit(playerImg, (x, y))


# Enemy function:
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


# Fire bullet function:
def fire_bullet(x, y):
    global bullet_state  # It brings the value of 'bullet_state' inside the function.
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y))


def is_Collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    # Tip for another user: distance = math.hypot(enemyX - bulletX, enemyY - bulletY)
    if distance < 27:
        return True
#    else: this code can be added but it's not necessary
# return False

# Game Loop:
running = True
while running:

    screen.fill((0, 0, 0))  # RGB Value.
    # Background image:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If I write pygame.quit or pygame.Quit or pygame.QUIT() I get an error.
            # It's QUIT all with capital letters and without the parentheses.
            running = False

        # If keystroke is pressed check whether it is right or left:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    # Get the current x coordinate of the spaceship.
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    # Player boundaries:
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736

    # Enemy movement:
    for i in range(num_of_enemies):

        # Game Over:
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000 # To put the enemies out of the screen.
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
        if enemyX[i] >= 736:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]

        # Collision:
        collision = is_Collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 100)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet movement:
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":  # Teacher wrote 'if bullet_state is fire' but python corrected me and told me to put ==
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()

pygame.quit()