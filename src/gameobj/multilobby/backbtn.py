from __future__ import annotations

from overrides import overrides
from typing import TYPE_CHECKING
import pygame

from gameobj.txtbtnobj import TextButtonObject
from util.resource_manager import font_resource
import util.colors as color

if TYPE_CHECKING:
    from manager.scenemgr import SceneManager


class BackButton(TextButtonObject):
    @overrides
    def start(self) -> None:
        screen_rect = pygame.display.get_surface().get_rect()
        self.font = pygame.font.Font(
            font_resource("MainFont.ttf"), screen_rect.height // 16
        )
        self.color = color.white
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect()
        self.topleft = (screen_rect.height // 32, screen_rect.height // 32)
        return None

    def attach_mgr(self, scene_manager: SceneManager) -> BackButton:
        self.scene_manager = scene_manager
        return self

    @overrides
    def on_click(self) -> None:
        self.scene_manager.load_previous_scene()
        return None

    pass
