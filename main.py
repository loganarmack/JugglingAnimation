import pygame
from pygame.locals import K_ESCAPE
import constant
import colours
from ball import Ball
from cascade import cascade_path

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SCREEN_W = screen.get_width()
SCREEN_H = screen.get_height()
clock = pygame.time.Clock()

running = True
last_time = pygame.time.get_ticks()

Ball.set_screen_res((SCREEN_W, SCREEN_H))
Ball.add_path('cascade', cascade_path)


start_offset = cascade_path.get_period_thirds()
red_ball = Ball(colours.RED, 0)
green_ball = Ball(colours.GREEN, start_offset)
blue_ball = Ball(colours.BLUE, 2 * start_offset)
balls = [red_ball, green_ball, blue_ball]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    screen.fill(colours.BLACK)

    time_delta = pygame.time.get_ticks() - last_time
    last_time = pygame.time.get_ticks()

    for ball in balls:
        ball.move(time_delta / 1000)
        screen.blit(ball.surf, ball.rect)

    pygame.display.flip()

    clock.tick(constant.FPS)


pygame.quit()
