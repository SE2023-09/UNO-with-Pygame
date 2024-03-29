from overrides import overrides

from .scene import Scene
from gameobj.bgobj import BackgroundObject
from gameobj.cfgmenu.titletxt import TitleText
from gameobj.cfgmenu.backbtn import BackButton
from gameobj.cfgmenu.cfgrstbtn import ConfigResetButton
from gameobj.cfgmenu.mainbtn import MainMenuButton
from gameobj.cfgmenu.achvbtn import AcheivementsButton
from gameobj.cfgmenu.menukey import MenuKey
from gameobj.cfgmenu.menuval import MenuValue
from gameobj.cfgmenu.leftbtn import LeftButton
from gameobj.cfgmenu.rightbtn import RightButton
from gameobj.cfgmenu.keymenuval import KeyMenuValue
from gameobj.cfgmenu.keyinput import KeyInput
from gameobj.cfgmenu.keybindarea import KeyBindArea
from gameobj.cfgmenu.volkey import VolumeKey
from gameobj.cfgmenu.volbar import VolumeBar
import util.colors as color


class ConfigMenu(Scene):
    @overrides
    def start(self) -> None:
        self.game_objects = []

        self.instantiate(BackgroundObject(color.black))
        self.instantiate(TitleText("Configurations"))
        self.instantiate(BackButton("Back").attach_mgr(self.scene_manager))
        self.instantiate(ConfigResetButton("Reset").attach_mgr(self.scene_manager))
        self.instantiate(KeyInput().attach_mgr(self.scene_manager))

        if self.scene_manager.previous_scene_name != "main_menu":
            self.instantiate(MainMenuButton("Main Menu").attach_mgr(self.scene_manager))
            self.instantiate(
                AcheivementsButton("Achievements").attach_mgr(self.scene_manager)
            )
            pass

        MenuKey.destroy_all()
        self.instantiate(MenuKey("Screen Size"))
        self.instantiate(MenuKey("Fullscreen"))
        self.instantiate(MenuKey("Colorblind Mode"))
        self.instantiate(MenuKey("Key Settings"))
        self.instantiate(MenuKey("Left"))
        self.instantiate(MenuKey("Right"))
        self.instantiate(MenuKey("Up"))
        self.instantiate(MenuKey("Down"))
        self.instantiate(MenuKey("Select"))
        self.instantiate(MenuKey("Cancel"))

        MenuValue.destroy_all()
        self.instantiate(MenuValue("screen_size"))
        self.instantiate(MenuValue("fullscreen"))
        self.instantiate(MenuValue("colorblind_mode"))

        LeftButton.destroy_all()
        self.instantiate(LeftButton("screen_size").attach_mgr(self.scene_manager))
        self.instantiate(LeftButton("fullscreen").attach_mgr(self.scene_manager))
        self.instantiate(LeftButton("colorblind_mode").attach_mgr(self.scene_manager))

        RightButton.destroy_all()
        self.instantiate(RightButton("screen_size").attach_mgr(self.scene_manager))
        self.instantiate(RightButton("fullscreen").attach_mgr(self.scene_manager))
        self.instantiate(RightButton("colorblind_mode").attach_mgr(self.scene_manager))

        KeyMenuValue.destroy_all()
        self.instantiate(KeyMenuValue("left"))
        self.instantiate(KeyMenuValue("right"))
        self.instantiate(KeyMenuValue("up"))
        self.instantiate(KeyMenuValue("down"))
        self.instantiate(KeyMenuValue("select"))
        self.instantiate(KeyMenuValue("cancel"))

        KeyBindArea.destroy_all()
        self.instantiate(KeyBindArea("left"))
        self.instantiate(KeyBindArea("right"))
        self.instantiate(KeyBindArea("up"))
        self.instantiate(KeyBindArea("down"))
        self.instantiate(KeyBindArea("select"))
        self.instantiate(KeyBindArea("cancel"))

        VolumeKey.destroy_all()
        self.instantiate(VolumeKey("All"))
        self.instantiate(VolumeKey("BGM"))
        self.instantiate(VolumeKey("SFX"))

        VolumeBar.destroy_all()
        self.instantiate(VolumeBar().set_target("all"))
        self.instantiate(VolumeBar().set_target("bgm"))
        self.instantiate(VolumeBar().set_target("sfx"))

        return None
