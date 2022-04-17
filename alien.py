# -*- Coding: UTF-8 -*-
'''==================================
@Project -> File    : Project_Code -> alien.py
@IDE    : PyCharm
@Author    : 北天
@Date   : 2022/4/17  20:51
@Desa   : 管理外星人
'''

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""
    
    def __init__(self, ai_game):
        """初始化外星人并设置其起始位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        # 加载外星人图像并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # 存储外星人的精确水平位置
        self.x = float(self.rect.x)
        
    def check_edges(self):
        """如果外星人位于屏幕边缘。就返回True"""
        screen_rect = self.screen.get_rect()
        """
        如果外星人的rect的属性right大于或等于屏幕的rect的right属性，
        就说明外星人位于屏幕右边缘；
        如果外星人的rect的left属性小于或等于0，
        就说明外星人位于屏幕左边缘。
        """
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        """
        如果fleet_direction为1，
        就将外星人的当前x坐标增大alien_speed，
        从而将外星人向右移；如果fleet_direction为-1，
        就将外星人的当前x坐标减去alien_speed，
        从而将外星人向左移。
        """
        
    def update(self):
        """向坐或者向右移动外星人"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x