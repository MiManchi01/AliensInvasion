# -*- Coding: UTF-8 -*-
'''==================================
@Project -> File    : 练习.py -> bullet.py
@IDE    : PyCharm
@Author    : 北天
@Date   : 2022/4/16  20:37
@Desa   : 管理飞船子弹
'''

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """管理飞船所发射的子弹的类"""
    
    def __init__(self, ai_game):
        """在飞船当前位置创建一个子弹对象"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        # 在(0, 0)处创建一个表示子弹的矩形，再次设置正确的位置
        # 子弹的位置取决于飞船的位置
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        """
        将子弹的rect.midtop设置为飞船的rect.midtop。
        这样子弹将从飞船顶部出发，看起来像是从飞船中射出的。
        我们将子弹的[插图]坐标存储为小数值，
        以便能够微调子弹的速度。
        """
        self.rect.midtop = ai_game.ship.rect.midtop
        
        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)
        
    def update(self):
        """向上移动子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.settings.bullet_speed
        # 更新表示子弹的rect的位置
        self.rect.y = self.y
        
    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        
        """
        draw.rect()函数使用存储在self.color中的颜色
        填充表示子弹的rect占据的屏幕部分
        """
        pygame.draw.rect(self.screen, self.color, self.rect)
