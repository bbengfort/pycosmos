import pygame
import pygame.freetype

from pygame.sprite import Sprite
from pygame.rect import Rect


def create_surface_with_text(text, font_size, color, background_color):
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=color, bgcolor=background_color)
    return surface.convert_alpha()


class TextElement(Sprite):

    def __init__(self, center_position, text, font_size, color, background_color):
        self.mouse_over = False

        default_image = create_surface_with_text(
            text=text,
            font_size=font_size,
            color=color,
            background_color=background_color,
        )

        active_image = create_surface_with_text(
            text=text,
            font_size=font_size * 1.2,
            color=color,
            background_color=background_color,
        )

        self.images = [default_image, active_image]
        self.rects = [
            img.get_rect(center=center_position) for img in self.images
        ]

        super().__init__()

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos):
        self.mouse_over = self.rect.collidepoint(mouse_pos)

    def draw(self, surface):
        surface.blit(self.image, self.rect)