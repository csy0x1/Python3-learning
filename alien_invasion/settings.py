class Settings():
    #存储a_i游戏所有设置的类
    def __init__(self):
        #屏幕设置
        self.screen_width=1366
        self.screen_height=768
        self.bg_color=(230,230,230)
        self.ship_speed_factor=1.5  #飞船速度的设置
        #子弹设置
        self.bullet_speed_factor=1
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=60,60,60