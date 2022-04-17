# -*- Coding: UTF-8 -*-
'''==================================
@Project -> File    : Test.py -> settings.py
@IDE    : PyCharm
@Author    : 北天
@Date   : 2022/4/14  22:05
@Desa   : 存储游戏设置
'''

class Settings():
    """存储游戏《外星人入侵》中所有设置的类"""
    
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # 飞船设置
        self.ship_speed = 1.5
        
        # 子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        # 将未消失的子弹数限制为三颗
        self.bullets_allowed = 3
        
        # 外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1
        
