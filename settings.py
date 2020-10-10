import os
from pygame import Rect


class Settings:

    # 方向
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3

    BOX_SIZE = 50

    # 坦克类型
    HERO = 0
    ENEMY = 1

    # 0表示空白、1表示红墙、2表示铁墙、3表示草、4表示海、5表示鸟
    RED_WALL = 1
    IRON_WALL = 2
    WEED_WALL = 3
    WALLS = [
        f"resources/images/walls/{file}" for file in os.listdir("resources/images/walls/")
    ]
    MAP_ONE = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, ],
        [0, 1, 0, 0, 1, 3, 3, 1, 1, 2, 1, 1, 3, 3, 1, 0, 0, 1, 0, ],
        [0, 1, 0, 0, 1, 3, 3, 1, 1, 2, 1, 1, 3, 3, 1, 0, 0, 1, 0, ],
        [0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, ],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, ],
        [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, ],
        [0, 1, 3, 3, 3, 1, 0, 0, 0, 0, 0, 0, 0, 1, 3, 3, 3, 1, 0, ],
        [0, 1, 3, 3, 3, 1, 0, 0, 1, 1, 1, 0, 0, 1, 3, 3, 3, 1, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, ],
    ]

    # 爆炸的图片
    BOOMS = [
        "resources/images/boom/" + file for file in os.listdir("resources/images/boom")
    ]

    # 爆炸的音乐
    BOOM_MUSIC = "resources/musics/boom.wav"
    FIRE_MUSIC = "resources/musics/fire.wav"

    def __init__(self):
        # 游戏帧率
        self.fps = 60
        # 窗口信息
        self.window_title = "Tank War"
        self.box_rect = Rect(0, 0, Settings.BOX_SIZE, Settings.BOX_SIZE)
        self.screen_rect = Rect(0, 0, Settings.BOX_SIZE*19, Settings.BOX_SIZE*13)
        self.screen_color = (0, 0, 0)

        # 我方坦克
        self.hero_images = {
            Settings.LEFT:"./resources/images/hero/hero1L.gif",
            Settings.RIGHT:"./resources/images/hero/hero1R.gif",
            Settings.UP:"./resources/images/hero/hero1U.gif",
            Settings.DOWN:"./resources/images/hero/hero1D.gif"
        }
        self.hero_image_name = "./resources/images/hero/hero1U.gif"
        self.hero_speed = 1

        # 敌方坦克
        self.enemy_images = {
            Settings.LEFT: "./resources/images/enemy/enemy1L.gif",
            Settings.RIGHT: "./resources/images/enemy/enemy1R.gif",
            Settings.UP: "./resources/images/enemy/enemy1U.gif",
            Settings.DOWN: "./resources/images/enemy/enemy1D.gif"
        }
        self.enemy_count = 1
        self.enemy_speed = 1

        # 子弹
        self.bullet_image_name = "./resources/images/bullet/bullet.png"
        self.bullet_rect = Rect(0, 0, 5, 5)
        self.bullet_speed = 3
