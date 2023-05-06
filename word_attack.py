import random

class WordAttack:
    def __init__(self, game):
        self.game = game
        self.game.settings.lines = open(self.game.settings.word_list_loc).read().splitlines()
    def reset(self):
        # Word generator will generate a random word from a list of words
        self.game.settings.word_x = random.randint(100, 500)
        self.game.settings.word_y = 0
        self.game.settings.speed += 0.6
        self.game.settings.pressed_word = ""

    def draw(self):
        self.reset()
        self.game.settings.chosen_word = random.choice(self.game.settings.lines)
        self.game.settings.use_txt = self.game.font.render(self.game.settings.chosen_word, True, self.game.settings.word_color)