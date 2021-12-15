import pygame
import constant


class Ball(pygame.sprite.Sprite):

    SCREEN_RES = None
    paths = {}

    def __init__(self, colour, start_time, style="cascade"):
        super(Ball, self).__init__()
        start_x, start_y = self.paths[style].get_pos(start_time)
        self.time = start_time
        self.radius = constant.BALL_RADIUS
        self.colour = colour
        self.surf = pygame.Surface(
            (self.radius * 2, self.radius * 2), flags=pygame.SRCALPHA)
        self.rect = self.surf.get_rect(
            topleft=(start_x - self.radius, start_y - self.radius))
        self._redraw()

    def _redraw(self):
        self.surf.fill(pygame.Color(0, 0, 0, 0))
        pygame.draw.circle(self.surf, self.colour,
                           (self.radius, self.radius), self.radius)

    def move(self, time_delta):
        self.time += time_delta
        x, y = self.paths['cascade'].get_pos(self.time)
        self.rect.x = x - self.radius + constant.X_MARGIN
        self.rect.y = y - self.radius + constant.Y_MARGIN

    @classmethod
    def add_path(cls, name, path):
        cls.paths[name] = path

    @classmethod
    def set_screen_res(cls, res):
        cls.SCREEN_RES = res

    @classmethod
    def set_catch_height(cls, height):
        cls.CATCH_HEIGHT = height

    @classmethod
    def set_flight_time(cls, time):
        cls.FLIGHT_TIME = time
