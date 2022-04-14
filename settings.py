import os
from pygame import Rect


class Settings:

    # 游戏设置
    FPS = 60    # 游戏帧率
    GAME_NAME = "坦克大战"  # 游戏标题
    BOX_SIZE = 50   # 单位屏幕大小
    BOX_RECT = Rect(0, 0, BOX_SIZE, BOX_SIZE)   # 单位屏幕矩形
    SCREEN_RECT = Rect(0, 0, BOX_SIZE * 19, BOX_SIZE * 13)  # 屏幕矩形
    SCREEN_COLOR = (0, 0, 0)    # 屏幕颜色

    # 通用变量
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3

    # 地图
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
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0, ],
    ]

    # 音频
    BOOM_MUSIC = "resources/musics/boom.wav"
    FIRE_MUSIC = "resources/musics/fire.wav"
    HIT_MUSIC = "resources/musics/hit.wav"

    # 坦克类型
    HERO = 0
    ENEMY = 1

    # 我方坦克
    HERO_IMAGE_NAME = "./resources/images/hero/hero1U.gif"
    HERO_IMAGES = {
        LEFT: "./resources/images/hero/hero1L.gif",
        RIGHT: "./resources/images/hero/hero1R.gif",
        UP: "./resources/images/hero/hero1U.gif",
        DOWN: "./resources/images/hero/hero1D.gif"
    }
    HERO_SPEED = 2
    BOSS_IMAGE = "./resources/images/5.png"
    # 我方老家

    # 敌方坦克
    ENEMY_IMAGES = {
        LEFT: "./resources/images/enemy/enemy2L.gif",
        RIGHT: "./resources/images/enemy/enemy2R.gif",
        UP: "./resources/images/enemy/enemy2U.gif",
        DOWN: "./resources/images/enemy/enemy2D.gif"
    }
    ENEMY_COUNT = 5
    ENEMY_SPEED = 1

    # 子弹
    BULLET_IMAGE_NAME = "./resources/images/bullet/bullet.png"
    BULLET_RECT = Rect(0, 0, 5, 5)
    BULLET_SPEED = 5

    # 0表示空白、1表示红墙、2表示铁墙、3表示草、4表示海、5表示鸟
    RED_WALL = 1
    IRON_WALL = 2
    WEED_WALL = 3
    BOSS_WALL = 5
    WALLS = [
        # f"resources/images/walls/{file}" for file in os.listdir("resources/images/walls/")
        f"resources/images/walls/{i}.png" for i in range(6)
    ]

    # 爆炸的图片
    BOOMS = [
        # 这里可能也要改
        f"resources/images/boom/" + file for file in os.listdir("resources/images/boom")
    ]
    # os.listdir() 返回值并不保证按文件名排序
    # 也许加一个WALLS.sort()和BOOMS.sort()可能也行
    # 因为我是帮人远程解决的这个bug，没搭起来环境，所以您可以自己试一下
