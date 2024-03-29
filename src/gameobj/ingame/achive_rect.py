from __future__ import annotations
from abstrclass.subject import Subject

from gameobj.gameobj import GameObject
from player.player import Player
from game.game import Game
import util.colors as colors
from manager.cfgmgr import Config
from util.resource_manager import font_resource, image_resource
from manager.acvmgr import AchieveManager

import pygame
from overrides import overrides
from abstrclass.observer import Observer
from typing import Type, TYPE_CHECKING

if TYPE_CHECKING:
    from abstrclass.subject import Subject


class AchiveRect(GameObject):
    @overrides
    def __init__(
        self,
        surface: pygame.Surface,
        name: str = "GameObject",
        width: int = -1,
        height: int = -1,
        left: int = 0,
        top: int = 0,
        z_index: int = -1,
        key_index: int = -1,
    ) -> None:
        self.screen_size = Config().get_screen_resolution()
        self.move_fwd = False
        self.move_bwd = False
        self.fps = 60
        self.time_count = self.fps * 2
        super().__init__(
            surface,
            name,
            width,
            height,
            left,
            top,
            z_index,
            key_index,
        )

    @overrides
    def start(self) -> None:
        self.image = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        self.rect_copy = pygame.rect.Rect((0, 0), self.rect.size)
        pygame.draw.rect(
            self.image,
            color=colors.light_green,
            rect=self.rect_copy,
            border_radius=self.height // 2,
        )
        self.font = pygame.font.Font(
            font_resource("MainFont.ttf"), round(self.height / 2)
        )
        self.achive_text = self.font.render(" ", True, colors.white)

    def achive_text_update(self, idx):
        self.start()
        self.achive_text = self.font.render(
            f"{AchieveManager().get_achieve_text(idx)} 달성!", True, colors.white
        )
        # self.icon = pygame.image.load(f"res/img/achieve/a{idx+1}.png")
        self.icon = pygame.image.load(image_resource(f"achieve/a{idx+1}.png"))
        self.icon = pygame.transform.scale(self.icon, size=(self.height, self.height))
        self.image.blit(self.icon, (self.width / self.height * 2, self.height / 6))

    @overrides
    def update(self) -> None:
        if self.move_fwd is True:
            self.image.blit(
                self.achive_text, (self.width / self.height * 7, self.height / 6)
            )
            if self.top < 10:
                self.top += 1
            else:
                self.top = 10
                self.move_fwd = False
                self.move_bwd = True

        if self.move_bwd is True:
            if self.time_count > 0:
                self.time_count -= 1
                return None
            if self.top > -self.height:
                self.top -= 1
            else:
                self.top = -self.height
                self.move_bwd = False
                self.time_count = self.fps * 2
                self.start()
