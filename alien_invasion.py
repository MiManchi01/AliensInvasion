# -*- Coding: UTF-8 -*-
'''==================================
@Project -> File    : Test.py -> alien_invasion.py
@IDE    : PyCharm
@Author    : 北天
@Date   : 2022/4/14  21:18
@Desa   : 管理游戏资源和行为
'''

import sys
import pygame
from settings import Settings
from ship import Ship


class AliensInvasion():
    """管理游戏资源和行为的类"""
    
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        
        """调用函数pygame.init()来初始化背景设置"""
        pygame.init()
        
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        
        # 指定游戏窗口的尺寸大小
        # self.screen = pygame.display.set_mode((2560, 1600))
        """
        将这个显示窗口赋给属性self.screen，
        让这个类中的所有方法都能够使用它。
        """
        pygame.display.set_caption("Aliens_Invasion")
        
        # 设置背景色
        # self.bg_color = (230, 230, 230)
        
        self.ship = Ship(self)
        
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # # 监视键盘和鼠标事件
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         # 玩家点击游戏窗口的关闭按钮时退出游戏
            #         sys.sxit()
            # # 每次循环时都重绘屏幕
            # self.screen.fill(self.settings.bg_color)
            # self.ship.blitme()
            #
            # # 让最近绘制的屏幕可见
            # pygame.display.flip()
            """
            pygame.display.flip()将不断更新屏幕，以显示元素的新位置，
            并且在原来的位置隐藏元素，从而营造平滑移动的效果
            """
            self._check_events()
            self.ship.update()
            self._updata_screen()

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # 向右移动飞船
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    # 向左移动飞船
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _updata_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
    
        pygame.display.flip()

                
if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AliensInvasion()
    ai.run_game()

