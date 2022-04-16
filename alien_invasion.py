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
from bullet import Bullet


class AliensInvasion():
    """管理游戏资源和行为的类"""
    
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        
        """调用函数pygame.init()来初始化背景设置"""
        pygame.init()
        
        self.settings = Settings()
        
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
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
        self.bullets = pygame.sprite.Group()
        
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
            # self.bullets.update()
            self._update_bullets()
            
            # 删除超出屏幕范围的子弹
            # """
            # 因为不能从for循环遍历的列表或编组中删除元素，
            # 所以必须遍历编组的副本。我们使用方法copy()来设置for循环
            # 我们使用方法copy()来设置for循环，
            # 从而能够在循环中修改bullets。我们检查每颗子弹，
            # 看看它是否从屏幕顶端消失。如果是，就将其从bullets中删除。
            # """
            # for bullet in self.bullets.copy():
            #     if bullet.rect.bottom <= 0:
            #         self.bullets.remove(bullet)
            # # 使用函数调用print()显示当前还有多少颗子弹，以核实确实删除了消失的子弹。
            # # print(len(self.bullets))
            
            self._update_screen()

    def _check_events(self):
        """响应按键和鼠标事件"""
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        #     elif event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_RIGHT:
        #             # 向右移动飞船
        #             self.ship.moving_right = True
        #         elif event.key == pygame.K_LEFT:
        #             # 向左移动飞船
        #             self.ship.moving_left = True
        #     elif event.type == pygame.KEYUP:
        #         if event.key == pygame.K_RIGHT:
        #             self.ship.moving_right = False
        #         elif event.key == pygame.K_LEFT:
        #             self.ship.moving_left = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self , event):
        """响应按键"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        
    def _check_keyup_events(self , event):
        """响应松开"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            
    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组bullets中"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
    def _update_bullets(self):
        """更新子弹位置并删除消失的子弹"""
        # 更新子弹的位置
        self.bullets.update()
        
        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
    
        pygame.display.flip()

        
if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AliensInvasion()
    ai.run_game()

