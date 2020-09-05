import pygame
import pygame.freetype
import pytmx
import random
import pickle

pygame.init()

"""
###   Hello there! Thanks for playing my game :D
###
###   WORKING TITLE: Chirality
###
###   Font is Press Start 2P, which can be found at https://www.fontspace.com/codeman38/press-start-2p
###   Heart pictures modified from https://opengameart.org/content/heart-pixel-art
###   Tilesets from https://opengameart.org/content/whispers-of-avalon-grassland-tileset
###   Some images upscaled using Image Resizer (https://forums.rpgmakerweb.com/index.php?threads/image-resizer-specially-for-upscaling-pixel-art.45856/)
"""

# Game-wide constants
CLEAR     = (0,  0,  0,  0)
BLACK     = (0,   0,   0  )
DARKBLACK = (25,  25,  25 )
DARKGRAY  = (50,  50,  50 )
GRAY      = (200, 200, 200)
DARKGREY  = (50,  50,  50 )
GREY      = (200, 200, 200)
WHITE     = (255, 255, 255)
RED       = (255, 0,   0  )
GREEN     = (0,   255, 0  )
BLUE      = (0,   0,   255)

FONT = pygame.freetype.Font("font/PressStart2P.ttf")

FPS = 60


# Setup
pygame.display.set_caption("Chirality")
gameicon = pygame.image.load('gameicon.png')
pygame.display.set_icon(gameicon)
screen = pygame.display.set_mode((640, 480), pygame.FULLSCREEN)
gameMap = pytmx.load_pygame("map\default.tmx", pixelalpha=True)


# Images
menu_background = pygame.image.load("images/menu/background.png").convert_alpha()

player_heart_full_small = pygame.image.load("images/player/heart/heart_16.png").convert_alpha()
player_heart_full_large = pygame.image.load("images/player/heart/heart_32.png").convert_alpha()
player_heart_half_small = pygame.image.load("images/player/heart/heart_16_half.png").convert_alpha()
player_heart_half_large = pygame.image.load("images/player/heart/heart_32_half.png").convert_alpha()
player_left_spritesheet  = pygame.image.load("images/player/spritesheet/playerleft.png").convert_alpha()
player_right_spritesheet = pygame.image.load("images/player/spritesheet/playerright.png").convert_alpha()
player_left_spritesheet_large  = pygame.image.load("images/player/spritesheet/playerleft_large.png").convert_alpha()
player_right_spritesheet_large = pygame.image.load("images/player/spritesheet/playerright_large.png").convert_alpha()


# Exit func
def close():
    pygame.quit()
    raise SystemExit("User has closed program, or there was a CRITICAL ERROR - anyways, bye for now :)")


# Necessary vars
menu_new, menu_new_rect = FONT.render("new", WHITE, size=36)
menu_load, menu_load_rect = FONT.render("load", WHITE, size=36)
menu_credits, menu_credits_rect = FONT.render("credits", WHITE, size=36)
menu_quit, menu_quit_rect = FONT.render("quit", WHITE, size=36)

leave_conf, leave_conf_rect = FONT.render("Are you sure?", WHITE, size=20)
leave_yes, leave_yes_rect = FONT.render("yes", WHITE, size=32)
leave_no, leave_no_rect = FONT.render("no", WHITE, size=32)


# Main Loop
end = False
flip = True
scene = 0
clock = pygame.time.Clock()
while not end:
    x,y = pygame.mouse.get_pos()
    
    if scene == 0: # Menu -----------------------------------------------------
        flip = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    scene = 4
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (x >= 50 and x <= 300) and (y >= 200 and y <= 250):
                    scene = 1 # New
                if (x >= 50 and x <= 300) and (y >= 250 and y <= 300):
                    scene = 2 # Load
                if (x >= 50 and x <= 300) and (y >= 300 and y <= 350):
                    scene = 3 # Credits
                if (x >= 50 and x <= 300) and (y >= 350 and y <= 400):
                    scene = 4 # Leave
    
        screen.fill(BLACK)
        screen.blit(menu_background, (0,0))

        if (x >= 50 and x <= 300) and (y >= 200 and y <= 250):
            pygame.draw.rect(screen, DARKGREY, pygame.Rect(45,195,260,50))
        screen.blit(menu_new, (50,200))

        if (x >= 50 and x <= 300) and (y >= 250 and y <= 300):
            pygame.draw.rect(screen, DARKGREY, pygame.Rect(45,245,260,50))
        screen.blit(menu_load, (50,250))

        if (x >= 50 and x <= 300) and (y >= 300 and y <= 350):
            pygame.draw.rect(screen, DARKGREY, pygame.Rect(45,295,260,50))
        screen.blit(menu_credits, (50,300))

        if (x >= 50 and x <= 300) and (y >= 350 and y <= 400):
            pygame.draw.rect(screen, DARKGREY, pygame.Rect(45,345,260,50))
        screen.blit(menu_quit, (50,350))
        
    elif scene == 1: # New --------------------------------------------------- TODO
        flip = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    scene = 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

        screen.fill(BLACK)

        for layer in gameMap.visible_layers:
            for x, y, gid, in layer:
                tile = gameMap.get_tile_image_by_gid(gid)
                screen.blit(tile, (x * gameMap.tilewidth,
                                   y * gameMap.tileheight))

    elif scene == 2: # Load -------------------------------------------------- TODO
        flip = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    scene = 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

        update_rect = pygame.Rect(320,190,300,205)
        screen.fill(BLACK)
        pygame.draw.rect(screen, GREY, update_rect, 10)

        pygame.display.update(update_rect)

    elif scene == 3: # Credits ----------------------------------------------- TODO
        flip = True

    elif scene == 4: # Leave -------------------------------------------------
        flip = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    scene = 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (x >= 430 and x <= 525) and (y >= 270 and y <= 315):
                    close() # yes
                if (x >= 430 and x <= 525) and (y >= 320 and y <= 365):
                    scene = 0 # no

        update_rect = pygame.Rect(320,190,300,205)
        screen.fill(BLACK)
        pygame.draw.rect(screen, GREY, update_rect, 10)
        screen.blit(leave_conf, (340, 210))
        if (x >= 430 and x <= 525) and (y >= 270 and y <= 315):
            pygame.draw.rect(screen, DARKGREY, pygame.Rect(425,265,100,48))
        screen.blit(leave_yes, (430, 270))
        if (x >= 430 and x <= 525) and (y >= 320 and y <= 365):
            pygame.draw.rect(screen, DARKGREY, pygame.Rect(425,315,100,48))
        screen.blit(leave_no, (445, 330))
        
        pygame.display.update(update_rect)

    else: # OwO undefined ----------------------------------------------------
        close()

    if flip:
        pygame.display.flip()
    clock.tick(FPS)
