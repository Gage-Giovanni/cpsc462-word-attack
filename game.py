import pygame as pg
from settings import Settings
from word_attack import WordAttack
import sys


class Game:
    def __init__(self):
        # Used to Initialize PyGame
        pg.init()

        # Calls the Settings(), which contains all the variables needed for the game
        self.settings = Settings()
        self.font = pg.font.SysFont(self.settings.font_family, self.settings.font_size)
        self.score_font = pg.font.SysFont(self.settings.score_font_family, self.settings.score_font_size)

        # Sets the screen and displays caption for the program
        self.screen = pg.display.set_mode((self.settings.x, self.settings.y))
        pg.display.set_caption(self.settings.game_title)

        # Calls the word generator to display the first word
        self.word_attack = WordAttack(game=self)
        self.word_attack.draw()

    def reset(self):
        # Resets all class values into the original position
        self.settings.speed = 0.03
        self.settings.point = 0
        self.word_attack.draw()
    def draw(self):
        # Draw creates the screen, adds the background, sets the speed, and also imports the words and
        # backgrounds
        self.screen.fill(self.settings.bg)
        self.settings.word_y += self.settings.speed
        self.screen.blit(self.settings.use_txt, (self.settings.word_x, self.settings.word_y))
        self.settings.point_caption = self.score_font.render(str(self.settings.point), True, self.settings.score_color)
        self.screen.blit(self.settings.point_caption, (10, 5))
    def event_watcher(self, e):
        if e.type == pg.QUIT:
            sys.exit()
        elif e.type == pg.KEYDOWN:
            self.settings.pressed_word += pg.key.name(e.key)
            if self.settings.chosen_word.startswith(self.settings.pressed_word):
                if self.settings.chosen_word == self.settings.pressed_word:
                    self.settings.point += len(self.settings.chosen_word)
                    self.word_attack.draw()
            else:
                self.settings.pressed_word = ""
    def play(self):
        # Game loop
        while True:
            self.draw()
            for e in pg.event.get():
                self.event_watcher(e=e)

            if self.settings.word_y < (self.settings.y - 5):
                pg.display.update()
            else:
                e = pg.event.wait()
                if e.type == pg.KEYDOWN and e.key == pg.K_SPACE:
                    self.reset()

def main():
    # System Fonts
    #print(pg.font.get_fonts())
    x = Game()
    x.play()

if __name__ == "__main__":
    main()
