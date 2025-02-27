class Settings(object):
    """docstring for Settings"""
    def __init__(self):
        # initialize setting of game

        # screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.game_bg_color = (238, 230, 133)
        self.force_const = 0.15

        # level settings
        self.level_bg_color = (255, 255, 255)
        self.level_button_color = (160,160,160)

        # ball settings
        self.ball_size = (73, 40)
        self.ball_iniPos = (492, 364)
        self.ball_iniCol = "red"
        self.ball_color_order = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]
        self.ball_left = 0 # 0 or -1
        self.ball_right = 0 # 0 or 1
        self.ball_speed = 0
        self.ball_speed_limit_low = 2
        self.ball_speed_limit_mid = 3
        self.ball_speed_limit_hig = 4

        # Biofilm settings
        self.color_order = ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "white"]
        self.film_speed = 1
        self.top_timer_limit = 8
        self.bottom_timer_limit = 3
        self.film_lambda = 1/6

        # slots settings
        self.slot_width = 128

        # Bomb settings
        self.bomb_up_limit = 11
        self.bomb_down_limit = 5
        self.bomb_up_limit_gosky = 3
        self.bomb_down_limit_gosky = 1
        self.bomb_size = (62, 59)
        self.bomb_safe_distance = 5
        self.bomb_speed = 1
        # demon settings
        self.demon_pos = (850, 50)
