import pygame, sys
class Settings:
    def __init__(self):
        # Game Title
        self.game_title = "WORD ATTACK!"

        # WORD LIST
        self.word_list_loc = "words.txt"

        # SCORE LIST
        self.score_list_loc = "scores.txt"

        # BG, Score, Word Colors
        self.bg = (0, 0, 0)
        self.word_color = (255, 255, 255)
        self.score_color = (105, 179, 240)

        # Define Screen Size
        self.x = 1280
        self.y = 720

        # Determine Speed / Point
        self.speed = 0.03
        self.point = 0

        # Font Settings
        self.font_family = "calibri"
        self.font_size = 48
        self.score_font_family = "arialblack"
        self.score_font_size = 32

        # Word Generator Settings
        self.chosen_word = None
        self.pressed_word = None
        self.word_x = None
        self.word_y = None
        self.use_txt = None
        self.point_caption = None
        self.lines = None
        self.gameover = "Game Over"