import pygame
import constant

THROW_NEXT = pygame.USEREVENT + 1
throw_event = pygame.event.Event(THROW_NEXT)

class Ball(pygame.sprite.Sprite):

    SCREEN_RES = None
    prev_throw = 1

    def __init__(self, colour, start, vx, vy, caught=True):
        super(Ball, self).__init__()
        self.radius = constant.BALL_RADIUS
        self.colour = colour
        self.vx = vx
        self.vy = vy
        self.surf = pygame.Surface((self.radius * 2, self.radius * 2), flags=pygame.SRCALPHA)
        self.rect = self.surf.get_rect(topleft=(start[0] - self.radius, start[1] - self.radius))
        self.caught = caught
        self.catch_height = 3 * Ball.SCREEN_RES[1]/4 - self.radius
        self._redraw()

    def _redraw(self):
        self.surf.fill(pygame.Color(0, 0, 0, 0))
        pygame.draw.circle(self.surf, self.colour, (self.radius, self.radius), self.radius)

    def move(self):
        if not self.caught:
            if self.vy > 0:
                distance_to_catch = self.catch_height - self.rect.y
                if distance_to_catch < self.vy:
                    self.vy = distance_to_catch
            self.rect.move_ip(self.vx, self.vy)
            self.vy += constant.GRAVITY
            if self.rect.y == self.catch_height:
                self._catch()

        else:
            self.rect.move_ip(self.vx, self.vy)
            

    def _catch(self):
        self.vy = 0
        self.vx = -0.5*self.vx
        self.caught = True
        pygame.event.post(throw_event)

    def throw(self):
        self.vy = -constant.THROW_VY
        self.caught = False
        self.vx = constant.THROW_VX * Ball.prev_throw
        Ball.prev_throw *= -1

    @classmethod
    def set_screen_res(cls, res):
        cls.SCREEN_RES = res
