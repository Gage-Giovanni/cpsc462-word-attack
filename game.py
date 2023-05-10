import pygame as pg
from settings import Settings
from word_attack import WordAttack
from button import Button
import sys
from leaderboard import addScore
import pygame_textinput
from leaderboard import getSortedLeaders
pg.init()

#play background music and set sound effect variables
music = pg.mixer.music.load("space_music.mp3")
correct_sound = pg.mixer.Sound("correct_input_sound.mp3")
gameover_sound = pg.mixer.Sound("gameover_sound.mp3")
pg.mixer.music.play(-1)
#Set the screen and font variables throught the game
SCREEN = pg.display.set_mode((1280, 720))
def get_font(size): 
    return pg.font.Font("assets/Space.ttf", size)




class Game:
    def __init__(self):
        # Used to Initialize PyGame
        pg.init()

        # Calls the Settings(), which contains all the variables needed for the game
        self.settings = Settings()
        self.font = pg.font.Font(self.settings.font_family, self.settings.font_size)
        self.score_font = pg.font.Font(self.settings.score_font_family, self.settings.score_font_size)

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

        # Loads the Graphics for the Game
        moon_img = pg.image.load("assets/star_moon_bg.jpg")
        building_img = pg.image.load("assets/buildings.jpg")
        score_rect_area = pg.image.load("assets/score_rect.jpg")
        score_icon_area = pg.image.load("assets/score_icon.jpg")
        self.screen.blit(moon_img, (0,0))
        self.screen.blit(building_img, (0, 500))
        self.screen.blit(score_rect_area, (20, 20))
        self.screen.blit(score_icon_area, (50, 50))

        self.settings.word_y += self.settings.speed
        self.screen.blit(self.settings.use_txt, (self.settings.word_x, self.settings.word_y))
        self.settings.point_caption = self.score_font.render(str(self.settings.point), True, self.settings.score_color)
        # Displays Point Value
        self.screen.blit(self.settings.point_caption, (115, 50))
    def event_watcher(self, e):
        if e.type == pg.QUIT:
            addScore(self.user, self.settings.point)
            sys.exit()
        elif e.type == pg.KEYDOWN:
            self.settings.pressed_word += pg.key.name(e.key)
            if self.settings.chosen_word.startswith(self.settings.pressed_word):
                if self.settings.chosen_word == self.settings.pressed_word:
                    correct_sound.play()
                    self.settings.point += len(self.settings.chosen_word)
                    score = self.settings.point
                    self.word_attack.draw()
            else:
                self.settings.pressed_word = ""
    def play(self):
        # Game loop
        pg.mixer.music.play(-1)
        self.get_username()
        while True:
            self.draw()
            for e in pg.event.get():
                self.event_watcher(e=e)

            if self.settings.word_y < (self.settings.y - 5):
                pg.display.update()
            else:
                pg.mixer.music.stop()
                gameover_sound.play()
                addScore(self.user, self.settings.point)
                gameOverScreen(self.settings.point)
                e = pg.event.wait()
                gameover_sound.stop()
                if e.type == pg.KEYDOWN and e.key == pg.K_SPACE:
                    pg.mixer.music.play(-1)
                    self.reset()

def main():
    # System Fonts
    #print(pg.font.get_fonts())
    x = Game()
    x.play()
def play():
    while True:
        main()
        #Parameters for quitting game and buttons reaction
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pg.display.update()
def LEADER_BOARD():
    while True:
        #set the basic backsreen and pointer
        LEADER_BOARD_POS = pg.mouse.get_pos()
        SCREEN.fill("Black")

        #Create the text for the leadboard title
        LEADER_BOARD_TEXT = get_font(75).render("Leaderboard", True, "White")
        LEADER_BOARD_RECT = LEADER_BOARD_TEXT.get_rect(center=(640, 60))
        SCREEN.blit(LEADER_BOARD_TEXT, LEADER_BOARD_RECT)

        #Retrieve and display top ten scores
        high_scores = getSortedLeaders()[:10]
        position = [640, 155]
        for score in high_scores:
            SCORE_TEXT = get_font(30).render(score['name'] + " - " + str(score['score']), True, "White")
            SCORE_RECT = SCORE_TEXT.get_rect(center = position)
            SCREEN.blit(SCORE_TEXT, SCORE_RECT)
            position[1] += 45

        #Create the return button to main menu
        LEADER_BOARD_BACK = Button(image=None, pos=(640, 650), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
        LEADER_BOARD_BACK.changeColor(LEADER_BOARD_POS)
        LEADER_BOARD_BACK.update(SCREEN)

        #Parameters for quitting game and buttons reaction
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if LEADER_BOARD_BACK.checkForInput(LEADER_BOARD_POS):
                    main_menu()

        pg.display.update()
def gameOverScreen(score):
     while True:
        #set the basic backsreen and pointer
        SCREEN.fill("Black")
        gameOverScreen_MOUSE_POS = pg.mouse.get_pos()

        #create text incuding Screen, Score text, actual Score
        gameOverScreen_TEXT = get_font(55).render("GAME OVER", True, "Red")
        gameOverScreen_RECT = gameOverScreen_TEXT.get_rect(center=(640, 100))
        score_TEXT = get_font(55).render("score:", True, "GREEN")
        score_RECT = score_TEXT.get_rect(center=(600, 250))
        scoreNumber_TEXT = get_font(55).render(str(score), True, "GREEN")
        scoreNumber_RECT = scoreNumber_TEXT.get_rect(center=(745, 250))

        #Display the text created
        SCREEN.blit(gameOverScreen_TEXT, gameOverScreen_RECT)
        SCREEN.blit(score_TEXT, score_RECT)
        SCREEN.blit(scoreNumber_TEXT, scoreNumber_RECT)

        #Create a button to return to main menu
        gameOverScreen_BACK = Button(image=pg.image.load("assets/Play Rect.png"), pos=(640, 400), 
                            text_input="MAIN MENU", font=get_font(30), base_color="White", hovering_color="Green")
        gameOverScreen_BACK.changeColor(gameOverScreen_MOUSE_POS)
        gameOverScreen_BACK.update(SCREEN)

        #Parameters for quitting game and button reaction
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if gameOverScreen_BACK.checkForInput(gameOverScreen_MOUSE_POS):
                    main_menu()
        pg.display.update()
def main_menu():
    while True:

        #set the basic backsreen and pointer 
        SCREEN.fill("Black")
        MENU_MOUSE_POS = pg.mouse.get_pos()

        #Create the text for the games title
        MENU_TEXT = get_font(90).render("Word Attack", True, "Red")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        #Create the three buttons for the main menu PLAY, LEADERBOARD, and QUIT
        PLAY_BUTTON = Button(image=pg.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="Green")
        LEADER_BOARD_BUTTON = Button(image=pg.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="LEADER BOARD", font=get_font(60), base_color="#d7fcd4", hovering_color="Green")
        QUIT_BUTTON = Button(image=pg.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="Green")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        #Have the text change color when mouse hovering over a button
        for button in [PLAY_BUTTON, LEADER_BOARD_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
            
        #Parameters for quitting game and buttons reaction
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if LEADER_BOARD_BUTTON.checkForInput(MENU_MOUSE_POS):
                    LEADER_BOARD()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pg.quit()
                    sys.exit()

        pg.display.update()
main_menu()