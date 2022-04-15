# -*- Coding: UTF-8 -*-
'''==================================
@Project -> File    : Test.py -> ship.py
@IDE    : PyCharm
@Author    : 北天
@Date   : 2022/4/14  22:21
@Desa   : 管理飞船
'''

import pygame


class Ship():
    """管理飞船的类"""
    
    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        
        # 将屏幕赋给了Ship的一个属性，以便在这个类的所有方法中轻松访问
        self.screen = ai_game.screen
        """使用方法get_rect()访问屏幕的属性rect，
        并将其赋给了self.screen_rect，
        这让我们能够将飞船放到屏幕的正确位置。
        """
        self.screen_rect = ai_game.screen.get_rect()
        
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        # 对于每艘新飞船，都将其放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom
        
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        
        def update(self):
            """根据移动标志调整飞船的位置"""
            if self.moving_right:
                self.rect.x += 1
            if self.moving_left:
                self.rect.x -= 1
        
        def blitme(self):
            """在指定位置绘制飞船"""
            self.screen.blit(self.image, self.rect)
