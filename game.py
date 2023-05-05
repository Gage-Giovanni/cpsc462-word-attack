import pygame as pg
from settings import Settings
from word_attack import WordAttack
import sys
from leaderboard import addScore
import pygame_textinput


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

    # Asks user to input their username for leaderboard purposes
    def get_username(self):
        username_font = pg.font.Font("assets/Space.ttf", 65)

        # Create TextInput-object
        textinput = pygame_textinput.TextInputVisualizer(cursor_color = 'white', font_color = 'white', font_object = username_font)

        clock = pg.time.Clock()

        prompt_position = [self.settings.x/2, self.settings.y/3]
        username_position = [self.settings.x/2, self.settings.y/3 + 90]

        while True:
            self.screen.fill(self.settings.bg)

            events = pg.event.get()

            # Feed text input visualizer with events every frame
            textinput.update(events)

            # Blit its surface onto the screen
            prompt_text = username_font.render('ENTER USERNAME', True, 'white')
            prompt_rect = prompt_text.get_rect(center = prompt_position)
            
            username_rect = textinput.surface.get_rect(center = username_position)

            self.screen.blit(prompt_text, prompt_rect)
            self.screen.blit(textinput.surface, username_rect)

            for event in events:
                if event.type == pg.QUIT:
                    sys.exit()
                if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                    self.user = textinput.value
                    return

            pg.display.update()
            clock.tick(30)
        

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
            addScore(self.user, self.settings.point)
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
        self.get_username()
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
                    addScore(self.user, self.settings.point)
                    self.reset()

def main():
    # System Fonts
    #print(pg.font.get_fonts())
    x = Game()
    x.play()

if __name__ == "__main__":
    main()
