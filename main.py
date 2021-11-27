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
THROW_NEXT = pygame.USEREVENT + 1

Ball.set_screen_res((SCREEN_W, SCREEN_H))

start_time = pygame.time.get_ticks()
balls = deque()
running = True


catch_height = 3 * Ball.SCREEN_RES[1]/4 - constant.BALL_RADIUS
max_height = catch_height - constant.THROW_VY ** 2 / (2 * constant.GRAVITY)
flight_time = constant.THROW_VY / constant.GRAVITY
red_offset = 0.5*constant.THROW_VX*flight_time

red_start = (SCREEN_W/4 + red_offset, 3*SCREEN_H/4)
red_ball = Ball(colours.RED, red_start, 0, 0)
green_start = (3*SCREEN_W/4 - red_offset, 3*SCREEN_H/4)
green_ball = Ball(colours.GREEN, green_start, 0, 0)
blue_start = (SCREEN_W/2 - constant.BALL_RADIUS * 2, max_height)
blue_ball = Ball(colours.BLUE, blue_start, -constant.THROW_VX, 0, False)

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

        if event.type == THROW_NEXT:
            ball = balls.popleft()
            ball.throw()
            balls.append(ball)

    time = pygame.time.get_ticks() - start_time

    screen.fill(colours.BLACK)
    
    for ball in balls:
        ball.move()
        screen.blit(ball.surf, ball.rect)

    pygame.display.flip()

    clock.tick(constant.FPS)


pygame.quit()
