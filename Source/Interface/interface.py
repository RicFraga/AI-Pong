import pygame
import numpy as np

WIDTH = 1200
HEIGHT = 600
BORDER = 20

fgColor = pygame.Color((0, 0, 0))
borderColor = pygame.Color((179, 179, 179))
ballColor = pygame.Color((12, 69, 200))
palColor = pygame.Color((128, 90, 73))

ballSpeedx = 0.2
ballSpeedy = 0.25

playerSpeed = 0.0001

class Ball:
    
    RADIUS = 10

    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def show(self, colour):
        global screen
        pygame.draw.circle(screen,
            colour,
            (self.x, self.y),
            self.RADIUS)

    def update(self):
        global fgColor, ballColor
        self.show(fgColor)

        if(self.y + self.vy + self.RADIUS >= HEIGHT - BORDER or self.y + self.vy - self.RADIUS <= BORDER):
            self.vy = -self.vy

        if(self.x + self.vx  + self.RADIUS >= WIDTH - BORDER or self.x + self.vx  - self.RADIUS <= BORDER):
            self.vx = -self.vx

        self.x += self.vx
        self.y += self.vy
        self.show(ballColor)

class Paddle:
    
    PWIDTH = 30
    PHEIGHT = 120

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self, colour):
        global palColor
        pygame.draw.rect(screen,
        colour,
        pygame.Rect((self.x, self.y), (self.PWIDTH, self.PHEIGHT)))\
    
    def update(self):
        global fgColor, palColor
        self.show(fgColor)

        if(pygame.mouse.get_pos()[1] <= BORDER):
            self.y = BORDER
        
        elif(pygame.mouse.get_pos()[1] >= HEIGHT - BORDER - Paddle.PHEIGHT):
            self.y = HEIGHT - BORDER - Paddle.PHEIGHT

        else:
            self.y = pygame.mouse.get_pos()[1]
        self.show(palColor)

auxballSpeedx = ballSpeedx
if(np.random.randint(2) == 0):
    auxballSpeedx = -ballSpeedx

auxballSpeedy = ballSpeedy
if(np.random.randint(2) == 0):
    auxballSpeedy = -ballSpeedy

ballplay = Ball(WIDTH // 2, HEIGHT // 2, auxballSpeedx, auxballSpeedy)
player1 = Paddle(BORDER, 240)
player2 = Paddle(WIDTH - BORDER - Paddle.PWIDTH, 240)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.draw.rect(screen,
                borderColor,
                pygame.Rect((0, 0), (WIDTH, BORDER)))

pygame.draw.rect(screen,
                borderColor,
                pygame.Rect(0 , 0, BORDER, HEIGHT))

pygame.draw.rect(screen,
                borderColor,
                pygame.Rect(0 , HEIGHT - BORDER, WIDTH, BORDER))

pygame.draw.rect(screen,
                borderColor,
                pygame.Rect(WIDTH - BORDER, 0 - BORDER, BORDER, HEIGHT))

ballplay.show(ballColor)
player1.show(palColor)
player2.show(palColor)

while(True):
    e = pygame.event.poll()
    if(e.type == pygame.QUIT):
        break

    ballplay.update()
    pygame.display.flip()
    keys = pygame.key.get_pressed()
    
    player1.update()

pygame.quit()