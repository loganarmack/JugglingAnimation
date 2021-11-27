import pygame
from pygame.locals import K_ESCAPE
import constant
import colours
from ball import Ball
from collections import deque

pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
SCREEN_W = screen.get_width()
SCREEN_H = screen.get_height()
clock = pygame.time.Clock()

last_throw_time = pygame.time.get_ticks()
balls = deque()
running = True


CATCH_HEIGHT = 3 * SCREEN_H/4 - constant.BALL_RADIUS
MAX_HEIGHT = CATCH_HEIGHT - constant.THROW_VY ** 2 / (2 * constant.GRAVITY)
FLIGHT_TIME = 2*constant.THROW_VY / constant.GRAVITY
RED_START_OFFSET = constant.CATCH_VX * FLIGHT_TIME / 2

Ball.set_screen_res((SCREEN_W, SCREEN_H))
Ball.set_catch_height(CATCH_HEIGHT)
Ball.set_flight_time(FLIGHT_TIME)

red_start = (SCREEN_W/4 + RED_START_OFFSET, 3*SCREEN_H/4)
red_ball = Ball(colours.RED, red_start)
green_start = (3*SCREEN_W/4, 3*SCREEN_H/4)
green_ball = Ball(colours.GREEN, green_start)
blue_start = (SCREEN_W/2 - constant.BALL_RADIUS * 2, MAX_HEIGHT)
blue_ball = Ball(colours.BLUE, blue_start, -constant.THROW_VX)

balls.append(green_ball)
balls.append(blue_ball)
balls.append(red_ball)

red_ball.throw()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        
    time_since_throw = pygame.time.get_ticks() - last_throw_time
    if time_since_throw > 500 * FLIGHT_TIME / constant.FPS:
        ball = balls.popleft()
        ball.throw()
        balls.append(ball)
        last_throw_time = pygame.time.get_ticks()

    screen.fill(colours.BLACK)
    
    for ball in balls:
        ball.move()
        screen.blit(ball.surf, ball.rect)

    pygame.display.flip()

    clock.tick(constant.FPS)


pygame.quit()
