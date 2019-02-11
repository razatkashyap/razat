import random
import time
import pygame
from threading import Thread

pygame.init()

#score counter
score = 0
set_time = 62

#main window coordinate
set_x = 600
set_y = 630

#snake coordinate
snake_x = 400
snake_y = 500
snake_width = 10
snake_height = 10

#extra parameter
run = True
vel = 10

#Apple coordinate
apple_x = round(random.randrange(0, set_x)/10.0)*10.0
apple_y = round(random.randrange(30, set_y)/10.0)*10.0
apple_width = 10
apple_height = 10

#Hurdle coordinate
hurdle_x = round(random.randrange(0, set_x)/10.0)*10.0
hurdle_y = round(random.randrange(30, set_y)/10.0)*10.0
hurdle_width = 10
hurdle_height = 10

#colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0, 0, 255)
hurdle = (80,50,120)

#game instructions
font = pygame.font.SysFont(None, 25)
small = pygame.font.SysFont(None, 15)

#main window creation
win = pygame.display.set_mode((set_x,set_y))
pygame.display.set_caption("Snake and Apple")

#Timers
start = int(time.time())
end = int(time.time() + set_time)
fixed = int(time.time())

#High Score File
hand = open("score.txt")
high = int(hand.read())

def over(message, color, x , y, countdown, go = False):
    outi = font.render(message, True, color)
    win.blit(outi, (x, y))
    pygame.display.update()
    time.sleep(countdown)
    global run
    run = go

#Intro
welcome = small.render("Welcome To", True, green)
win.blit(welcome, (270, 290))
over("Snake and Apple", red, 230, 310, 2, True)


while run :
    if start <= end:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and snake_y > vel + 10:
            snake_y -= vel
        if keys[pygame.K_DOWN] and snake_y < set_y - (snake_height-10) - vel:
            snake_y += vel
        if keys[pygame.K_RIGHT] and snake_x < set_x - (snake_width-10) - vel:
            snake_x += vel
        if keys[pygame.K_LEFT] and snake_x > vel - 10:
            snake_x -= vel
        if keys[pygame.K_q]:
            over("Game Over", red,  270, 310, 5)
        if keys[pygame.K_ESCAPE]:
            over("Good Bye", red, 270, 310, 1)

        if apple_x == snake_x and apple_y == snake_y:
            apple_x = round(random.randrange(0, (set_x-10)) / 10.0) * 10.0
            apple_y = round(random.randrange(30, (set_y-10)) / 10.0) * 10.0
            hurdle_x = round(random.randrange(0, set_x) / 10.0) * 10.0
            hurdle_y = round(random.randrange(30, set_y) / 10.0) * 10.0
            #snake_width += 10
            score += 1

        if hurdle_x == snake_x and hurdle_y == snake_y:
            over("Game Over", red, 270, 310, 5)

        win.fill(white)
        pygame.draw.rect(win, black, (snake_x, snake_y, snake_width, snake_height))
        pygame.draw.rect(win, red, (apple_x, apple_y, apple_width, apple_height))
        pygame.draw.rect(win, hurdle, (hurdle_x, hurdle_y, hurdle_width, hurdle_height))
        screen = font.render("Score : "+str(score), True, green)
        win.blit(screen, (510, 0))
        highScore = "High Score : "+str(high)
        message = font.render(highScore, True, blue)
        win.blit(message, (200, 0))
        timeLeft = "Time : " + str(set_time - (start - fixed))
        start = int(time.time())
        message = font.render(timeLeft, True, red)
        win.blit(message, (5, 0))
        pygame.display.update()
    else:
        if high <= score:
            handle = open("score.txt", "w")
            handle.write(str(score))
            handle.close()
        over("Game Over", red, 270, 310, 5)

hand.close()
pygame.quit()
quit()
