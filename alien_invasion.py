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
from alien import Alien


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
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        
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
            self._update_aliens()
            
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
        
        # # 检查是否有子弹击中了外星人
        # # 如果是，就删除相应的子弹和外星人
        # collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        #
        # if not self.aliens:
        #     # 删除现有的子弹并新建一群外星人
        #     self.bullets.empty()
        #     self._create_fleet()
        self._check_bullet_alien_ccollisions()
        
    def _check_bullet_alien_ccollisions(self):
        """响应子弹和外星人碰撞"""
        # 删除发生碰撞的子弹和外星人
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        
        if not self.aliens:
            # 删除现有的所有子弹，并创建一群新的外星人
            self.bullets.empty()
            self._create_fleet()
                
    def _update_aliens(self):
        """检查是否有外星人位于屏幕边缘，
        更新外星人群中所有外星人的位置。
        """
        self._check_fleet_edges()
        self.aliens.update()

    def _create_fleet(self):
        """创建外星人群"""
        # 创建一个外星人并计算一行可容纳多少个外星人
        # 外星人的间距为外星人的宽度
        alien = Alien(self)
        """
        从外星人的rect属性中获取外星人宽度，
        并将这个值存储到alien_width中，
        以免反复访问属性rect。
        """
        alien_width, alien_height= alien.rect.size
        # 计算可用于放置外星人的水平空间以及其中可容纳多少个外星人。
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        
        # 计算屏幕可容纳多少行外星人
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        
        # 创建外星人群
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
        
        # # 创建第一行外星人
        # for alien_number in range(number_aliens_x):
        #     # alien = Alien(self)
        #     # alien.x = alien_width + 2 * alien_width * alien_number
        #     # alien.rect.x = alien.x
        #     # self.aliens.add(alien)
        #     self._create_alien(alien_number)
            
    def _create_alien(self, alien_number, row_number):
        """创建一个外星人并将其放在当前行"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        """
        相邻外星人行的y坐标相差外星人高度的两倍，
        因此将外星人高度乘以2，再乘以行号。
        第一行的行号为0，因此第一行的垂直位置不变，
        而其他行都沿屏幕依次向下放置
        """
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)
        
    def _check_fleet_edges(self):
        """有外星人到达边缘时采取相应的措施"""
        for alien in self.aliens.sprites():
            """
            如果check_edges()返回True，
            就表明相应的外星人位于屏幕边缘，
            需要改变外星人群的方向，
            因此调用_change_fleet_direction()并退出循环
            """
            if alien.check_edges():
                self._change_fleet_direction()
                break
                
    def _change_fleet_direction(self):
        """将整群外星人下移。并改变它们的方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
            self.settings.fleet_direction *= -1

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()

        
if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AliensInvasion()
    ai.run_game()

