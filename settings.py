class Settings(object):
    """docstring for Settings"""
    def __init__(self):
        # initialize setting of game

        # screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.force_const = 0.15

        #ball settings
        self.ball_size = (40, 40)
        self.ball_iniPos = (492,364)
        self.ball_iniCol = "red"
        self.ball_color_order = ["red", "yellow", "green", "blue", "purple"]
        self.ball_left = 0 # 0 or -1
        self.ball_right = 0 # 0 or 1
        self.ball_speed = 0

        #Biofilm settings
        self.film_size = (4, 1024)
        self.film_iniPos = 1024
        self.color_order = ["red", "yellow", "green", "blue", "purple"]
        self.film_speed = 1
        self.film_lambda = 1/6