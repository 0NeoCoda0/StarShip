# Сначала появляются все звезды на небе
# Затем генерируются сверху экрана
# Входные параметры: группа_спрайтов, количество_генерируемых_звезд, (начальная_высота, конечная_высота)
# Результат: плоскость с непересекающимися звездами

from star import Star
from pygame.sprite import Sprite
from pygame.surface import Surface
from config import HEIGHT_SCREEN, WIDTH_SCREEN

class Sky(Sprite):
    def __init__(self, stars_quantity):
        self.stars_quantity = stars_quantity
        self.image = Surface (WIDTH_SCREEN, HEIGHT_SCREEN,)