import pygame

from game_logic.user_control import UserControl


class TextControl(UserControl):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__(x, y, width, height)

        self.text = ''
        self.back_color = (0, 0, 255)
        self.font_color = (255, 0, 255)
        self.font = 'arial'
        self.text_size = 36

    def draw(self, display):
        pygame.draw.rect(
            display, self.back_color,
            [self.x, self.y, self.width, self.height])

        text_surface = pygame.font.SysFont(self.font, self.height).render(self.text, True, self.font_color)
        display.blit(text_surface, (self.x, self.y))