from __future__ import annotations

from gameobj.gameobj import GameObject
import util.colors as colors

import pygame
from overrides import overrides
from abstrclass.observer import Observer
from typing import Type, TYPE_CHECKING

if TYPE_CHECKING:
    from abstrclass.subject import Subject


class Space(GameObject, Observer):
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
        color: tuple = colors.white,
    ) -> None:
        self.turn = False
        self.color = color
        self.turn_color = colors.red
        self.deck = False
        self.current_color = colors.white
        super().__init__(surface, name, width, height, left, top, z_index)

    @overrides
    def start(self):
        self.border = pygame.rect.Rect((0, 0), self.rect.size)
        if self.turn is True and self.deck is False:
            pygame.draw.rect(
                surface=self.image, color=self.turn_color, rect=self.border, width=2
            )
        elif self.turn is False and self.deck is False:
            pygame.draw.rect(
                surface=self.image, color=self.color, rect=self.border, width=2
            )

        if self.deck is True:
            self.image.fill(self.color)

    def observer_update(self, subject: Type[Subject]):
        discard_card = subject.get_discard_info().get("discarded_card")
        current_color = discard_card.get("color")

        if current_color == "wild":
            self.current_color = colors.black
        elif current_color == "red":
            self.current_color = colors.red
        elif current_color == "blue":
            self.current_color = colors.blue
        elif current_color == "green":
            self.current_color = colors.green
        elif current_color == "yellow":
            self.current_color = colors.yellow

    @overrides
    def update(self):
        # 턴 시작하면 테두리 색 변화
        if self.turn is True and self.deck is False:
            pygame.draw.rect(
                surface=self.image, color=self.turn_color, rect=self.border, width=2
            )
        elif self.turn is False and self.deck is False:
            pygame.draw.rect(
                surface=self.image, color=self.color, rect=self.border, width=2
            )

        if self.deck is True:
            self.image.fill(self.color)
            pygame.draw.circle(
                self.image,
                color=self.current_color,
                center=self.rect.center,
                radius=self.height / 2,
                width=25,
            )
