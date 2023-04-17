import pygame

from resource_manager import sound_resource


class SoundManager:
    def __init__(self):
        pygame.mixer.init()  # pygame.mixer 초기화
        self.background_sound = pygame.mixer.Sound(sound_resource("background.mp3"))
        self.deal_effect_sound = pygame.mixer.Sound(sound_resource("deal1.mp3"))
        self.discard_effect_sound = pygame.mixer.Sound(sound_resource("discard1.wav"))
        self.draw_effect_sound = pygame.mixer.Sound(sound_resource("draw1.wav"))
        self.shuffle_effect_sound = pygame.mixer.Sound(sound_resource("shuffle.mp3"))
        self.timeout_effect_sound = pygame.mixer.Sound(sound_resource("timeout.mp3"))
        self.click_effect_sound = pygame.mixer.Sound(sound_resource("click.mp3"))

        self.effect = {
            "deal": self.deal_effect_sound,
            "discard": self.discard_effect_sound,
            "draw": self.draw_effect_sound,
            "shuffle": self.shuffle_effect_sound,
            "timeout": self.timeout_effect_sound,
            "click": self.click_effect_sound,
        }

        self.is_background_playing = False

    def play_background_sound(self):
        if not self.is_background_playing:  # 배경음악이 재생중이 아니면
            self.background_sound.play(-1)  # 배경음악 재생
            self.is_background_playing = True  # 배경음악 재생중으로 표시

    def stop_background_sound(self):
        self.background_sound.stop()  # 배경음악 정지
        self.is_background_playing = False  # 배경음악 재생중이 아니라고 표시

    def set_background_sound_volume(self, volume):
        self.background_sound.set_volume(volume)  # 배경음악 음량 조절 0~1 사이값, 0은 음소거 1은 최대 볼륨

    def play_effect(self, name):
        if name in self.effect:
            self.effect[name].play()  # 효과음 재생

    def set_effect_volume(self, volume):
        for effect_sound in self.effect.values():
            effect_sound.set_volume(volume)  # 효과음 음량 조절 0~1 사이값, 0은 음소거 1은 최대 볼륨