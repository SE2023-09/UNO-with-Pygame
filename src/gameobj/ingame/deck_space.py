from __future__ import annotations

from gameobj.gameobj import GameObject
import util.colors as colors

import pygame
from overrides import overrides
from abstrclass.observer import Observer
from typing import Type, TYPE_CHECKING

if TYPE_CHECKING:
    from abstrclass.subject import Subject


class DeckSpace(GameObject, Observer):
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
        self.color = color
        self.current_color = colors.white
        self.reverse_turn = False
        super().__init__(surface, name, width, height, left, top, z_index)
        self.pt1 = (self.rect.centerx + self.height * 2 / 5 + 20, self.rect.centery)
        self.pt2 = (self.rect.centerx + self.height * 2 / 5 - 50, self.rect.centery)
        self.pt3 = (
            self.rect.centerx + self.height * 2 / 5 - 15,
            self.rect.centery + 40,
        )
        self.down_pt3 = self.pt3
        self.up_pt3 = (
            self.rect.centerx + self.height * 2 / 5 - 15,
            self.rect.centery - 40,
        )

    @overrides
    def start(self):
        self.image.fill(self.color)

    def observer_update(self, subject: Type[Subject]):
        # 컬러 업데이트
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

        # 턴방향 업데이트
        reverse_turn = subject._reverse_direction
        if reverse_turn is True:
            self.pt3 = self.up_pt3
        else:
            self.pt3 = self.down_pt3

    @overrides
    def update(self):
        self.image.fill(self.color)
        pygame.draw.circle(
            self.image,
            color=self.current_color,
            center=self.rect.center,
            radius=self.height * 2 / 5,
            width=30,
        )
        pygame.draw.polygon(
            surface=self.image,
            color=self.current_color,
            points=[self.pt1, self.pt2, self.pt3],
        )
        pygame.draw.line(
            surface=self.image,
            color=self.color,
            start_pos=self.pt1,
            end_pos=self.pt3,
            width=4,
        )
        pygame.draw.line(
            surface=self.image,
            color=self.color,
            start_pos=self.pt2,
            end_pos=self.pt3,
            width=4,
        )