from __future__ import annotations

from overrides import overrides
import pygame

from gameobj.txtobj import TextObject
from util.resource_manager import font_resource
from metaclass.singleton import SingletonMeta
import util.colors as color


class TextD(TextObject):
    @overrides
    def start(self) -> None:
        self.text = "D: 기술 카드 사용하지 않고 승리"
        screen_rect = pygame.display.get_surface().get_rect()
        self.font = pygame.font.Font(
            font_resource("MainFont.ttf"), screen_rect.height // 30
        )
        self.color = color.white
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect()
        self.z_index = 997
        return None

    pass
