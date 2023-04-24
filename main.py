import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

#BG = pygame.image.load("assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/Space.ttf", size)

def play():
    while True:
        #set the basic backsreen and pointer
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")

        #Create the text for the play screen for now
        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        #Create the return button to the main menu
        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        #Parameters for quitting game and buttons reaction
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    
def LEADER_BOARD():
    while True:
        #set the basic backsreen and pointer
        LEADER_BOARD_POS = pygame.mouse.get_pos()
        SCREEN.fill("Black")

        #Create the text for the leadboard for now
        LEADER_BOARD_TEXT = get_font(45).render("This is the LEADER BOARD screen.", True, "White")
        LEADER_BOARD_RECT = LEADER_BOARD_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(LEADER_BOARD_TEXT, LEADER_BOARD_RECT)

        #Create the return button to main menu
        LEADER_BOARD_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
        LEADER_BOARD_BACK.changeColor(LEADER_BOARD_POS)
        LEADER_BOARD_BACK.update(SCREEN)

        #Parameters for quitting game and buttons reaction
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEADER_BOARD_BACK.checkForInput(LEADER_BOARD_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:

        #set the basic backsreen and pointer 
        SCREEN.fill("Black")
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        #Create the text for the games title
        MENU_TEXT = get_font(90).render("Name Pending", True, "Red")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        #Create the three buttons for the main menu PLAY, LEADERBOARD, and QUIT
        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="Green")
        LEADER_BOARD_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="LEADER BOARD", font=get_font(60), base_color="#d7fcd4", hovering_color="Green")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="Green")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        #Have the text change color when mouse hovering over a button
        for button in [PLAY_BUTTON, LEADER_BOARD_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
            
        #Parameters for quitting game and buttons reaction
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if LEADER_BOARD_BUTTON.checkForInput(MENU_MOUSE_POS):
                    LEADER_BOARD()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()