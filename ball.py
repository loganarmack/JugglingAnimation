import pygame
import constant

THROW_NEXT = pygame.USEREVENT + 1
throw_event = pygame.event.Event(THROW_NEXT)

class Ball(pygame.sprite.Sprite):

    SCREEN_RES = None
    CATCH_HEIGHT = 0
    FLIGHT_TIME = 0
    prev_throw = 1

    def __init__(self, colour, start, vx=0):
        super(Ball, self).__init__()
        self.radius = constant.BALL_RADIUS
        self.colour = colour
        self.surf = pygame.Surface((self.radius * 2, self.radius * 2), flags=pygame.SRCALPHA)
        self.rect = self.surf.get_rect(topleft=(start[0] - self.radius, start[1] - self.radius))
        self.caught = vx == 0
        if self.caught:
            self.vx = -Ball.prev_throw * constant.CATCH_VX
            self.vy = constant.CATCH_VY
        else:
            self.vx = vx
            self.vy = 0
        self._redraw()

    def _redraw(self):
        self.surf.fill(pygame.Color(0, 0, 0, 0))
        pygame.draw.circle(self.surf, self.colour, (self.radius, self.radius), self.radius)

    def move(self):
        if not self.caught:
            if self.vy > 0:
                distance_to_catch = Ball.CATCH_HEIGHT - self.rect.y
                if distance_to_catch < self.vy:
                    self.vy = distance_to_catch
            self.rect.move_ip(self.vx, self.vy)
            self.vy += constant.GRAVITY
            if self.rect.y == Ball.CATCH_HEIGHT:
                self._catch()

        else:
            self.vy -= 2 * constant.CATCH_VY / Ball.FLIGHT_TIME
            self.rect.move_ip(self.vx, self.vy)
            

    def _catch(self):
        self.vy = constant.CATCH_VY
        self.vx = -constant.CATCH_VX*self.vx/abs(self.vx)
        self.caught = True

    def throw(self):
        self.vy = -constant.THROW_VY
        self.caught = False
        self.vx = constant.THROW_VX * Ball.prev_throw
        Ball.prev_throw *= -1

    @classmethod
    def set_screen_res(cls, res):
        cls.SCREEN_RES = res

    @classmethod
    def set_catch_height(cls, height):
        cls.CATCH_HEIGHT = height

    @classmethod
    def set_flight_time(cls, time):
        cls.FLIGHT_TIME = time
