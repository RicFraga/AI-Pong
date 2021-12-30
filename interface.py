import pygame

WIDTH = 1200
HEIGHT = 600
BORDER = 20

fgColor = pygame.Color((0, 0, 0))
borderColor = pygame.Color((179, 179, 179))
ballColor = pygame.Color((12, 69, 200))
palColor = pygame.Color((128, 90, 73))

ballSpeed = 0.15

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
        pygame.Rect((self.x, self.y), (self.PWIDTH, self.PHEIGHT)))

ballplay = Ball(WIDTH // 2, HEIGHT // 2, -ballSpeed, 0)
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

pygame.quit()