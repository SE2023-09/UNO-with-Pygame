from __future__ import annotations

import pygame
from overrides import overrides

from gameobj.gameobj import GameObject
from manager.cfgmgr import Config

from abstrclass.observer import Observer
from typing import Type, TYPE_CHECKING

if TYPE_CHECKING:
    from abstrclass.subject import Subject

# 게임에서 사용될 카드를 시작시 모두 로딩, not visible 상태
# 처음 분배된 카드는 순서에 맞춰서 유저와 봇 공간으로 이동
#  - 봇의 카드는 뒷면으로 로딩후, 가지고있는 수 만큼만 표시
#  - 유저의 카드는 순서를 나타내는 멤버변수를 가짐
#  - 유저 카드의 인덱스에 따른 위치를 game_scene에서 미리 정의한 뒤 해당하는 위치로 이동
#
# 드로우 더미에 있는 카드들은 드로우 될 순서에 따라 정렬되어 있는 상태이고 마우스 클릭시 맨 위 카드가 드로우 됨
#
# 카드를 드로우 하는 경우 드로우 더미 위치에서 해당하는 유저 카드 인덱스 위치로 이동
#  - 먼저 visible 상태로 바꾸기
#  - 기존의 카드들은 애니메이션 없이 이동
# 카드를 내는 경우 버린카드 더미 맨 위로 이동, visible
#
# 유저의 턴이 아닌 경우 모두 작동하지 않아야 함
#
# game_scene에서는 다음과 같은 정보를 계속 업데이트 해야함:
# 1. 유저 카드 숫자,색
# 2. 유저 카드들 각각의 인덱스(순서)


class Card(GameObject, Observer):
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
        code: int = -1,
        target_pos: tuple = (0, 0),
    ) -> None:
        super().__init__(surface, name, width, height, left, top, z_index)
        self.left = left
        self.top = top
        self.target_pos = target_pos
        self.code = code
        self.user = False
        self.ani = False
        self.discard_flag = False
        self.draw_flag = False
        self.user_turn = False

        settings = Config()
        screen_size = settings.get_screen_resolution()

        card_size = self.rect.size

        self.discard_pile_pos = (
            screen_size[0] * 3 / 8 + card_size[0],
            screen_size[1] * 1 / 3 - card_size[1] / 2,
        )
        self.user_card_pos = [
            (
                (i + 1) * card_size[0] * 3 / 4,
                screen_size[1] * (2 / 3) + card_size[1] / 2,
            )
            if i <= 14
            else (
                (i + 1) * card_size[0] * 3 / 4,
                screen_size[1] * (2 / 3) + card_size[1] * 3 / 2,
            )
            for i in range(40)
        ]

    @overrides
    def on_mouse_enter(self) -> None:
        self.rect.y -= 10

    @overrides
    def on_mouse_exit(self) -> None:
        self.rect.y += 10

    @overrides
    def on_mouse_down(self) -> None:
        if self.user_turn is True:
            self.ani = True
            self.discard_flag = True
        else:
            self.ani = False
            self.discard_flag = False

    def observer_update(self, subject: Type[Subject]):
        self.user_turn = subject.get_user().is_turn()
        # 카드 위치 재정렬
        if self.user is True:
            self.user_card_list = subject.get_user().get_hand_cards()
            for i, code in enumerate(self.user_card_list):
                if self.code == code:
                    self.rect.x = self.user_card_pos[i][0]
                    self.rect.y = self.user_card_pos[i][1]

        # 에니메이션
        # if self.ani is True:
        #     if (
        #         (self.rect.x < self.target_pos[0] and self.rect.y < self.target_pos[1])
        #         or (
        #             self.rect.x > self.target_pos[0]
        #             and self.rect.y < self.target_pos[1]
        #         )
        #         or (
        #             self.rect.x < self.target_pos[0]
        #             and self.rect.y > self.target_pos[1]
        #         )
        #     ):
        #         self.rect.x += (self.target_pos[0] - self.left) / 10 + 1
        #         self.rect.y += (self.target_pos[1] - self.top) / 10 + 1
        #     else:
        #         self.rect.x = self.target_pos[0]
        #         self.rect.y = self.target_pos[1]
        #         self.ani = False

    @overrides
    def update(self) -> None:
        if self.discard_flag is True:
            if (
                self.rect.x < self.target_pos[0] and self.rect.y > self.target_pos[1]
            ) or (
                self.rect.x > self.target_pos[0] and self.rect.y > self.target_pos[1]
            ):
                self.rect.x += (self.target_pos[0] - self.left) / 10 + 1
                self.rect.y += (self.target_pos[1] - self.top) / 10 + 1
            else:
                self.rect.x = self.discard_pile_pos[0]
                self.rect.y = self.discard_pile_pos[1]
                self.ani = False
                self._visible = False
                self.discard_flag = False

        if self.draw_flag is True:
            if (
                (self.rect.x < self.target_pos[0] and self.rect.y < self.target_pos[1])
                or (
                    self.rect.x > self.target_pos[0]
                    and self.rect.y < self.target_pos[1]
                )
                or (
                    self.rect.x < self.target_pos[0]
                    and self.rect.y > self.target_pos[1]
                )
            ):
                self.rect.x += (self.target_pos[0] - self.left) / 10 + 1
                self.rect.y += (self.target_pos[1] - self.top) / 10 + 1
            else:
                self.rect.x = self.target_pos[0]
                self.rect.y = self.target_pos[1]
                self.ani = False
                self.draw_flag = False
