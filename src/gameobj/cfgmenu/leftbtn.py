from __future__ import annotations

from overrides import overrides
from typing import TYPE_CHECKING
import pygame

from gameobj.txtbtnobj import TextButtonObject
from util.resource_manager import font_resource
from manager.cfgmgr import Config
import util.colors as color
from manager.soundmgr import SoundManager

if TYPE_CHECKING:
    from manager.scenemgr import SceneManager


class LeftButton(TextButtonObject):
    Inst_created: int = 0
    Insts: list[LeftButton] = []

    def __new__(cls, *args, **kwargs):
        cls.Inst_created += 1
        return super().__new__(cls)

    @overrides
    def start(self) -> None:
        self.soundmanager = SoundManager()
        LeftButton.Insts.append(self)
        screen_rect = pygame.display.get_surface().get_rect()
        self.font = pygame.font.Font(
            font_resource("MainFont.ttf"), screen_rect.height // 20
        )
        self.color = color.white
        self.target_config = self.text
        self.text = "<"
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect()
        self.topleft = (
            screen_rect.width * 4 // 8,
            screen_rect.height * (2 + self.Inst_created) // 16,
        )
        return None

    def attach_mgr(self, scene_manager: SceneManager) -> LeftButton:
        self.scene_manager = scene_manager
        return self

    @overrides
    def on_click(self) -> None:
        self.soundmanager.play_effect("click")
        Config().decrease(self.target_config)
        self.scene_manager.reload_scene()
        return None

    @overrides
    def on_destroy(self) -> None:
        LeftButton.Inst_created -= 1
        return None

    @staticmethod
    def destroy_all() -> None:
        for inst in LeftButton.Insts:
            inst.on_destroy()
            del inst
            pass
        LeftButton.Inst_created = 0
        return None

    pass
