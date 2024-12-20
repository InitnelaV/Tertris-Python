import pygame
import sys
from game import Game
from colors import Colors

pygame.init()
title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)

score_rect = pygame.Rect(445, 75, 220, 80)
next_rect = pygame.Rect(445, 235, 220, 120)
screen = pygame.display.set_mode((700, 820))
pygame.display.set_caption("Te7ris")

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()

        score_value_surface = title_font.render(str(game.score), True, Colors.white)

        screen.fill(Colors.dark_blue)
        screen.blit(score_surface, (520, 30, 70, 70))
        screen.blit(next_surface, (530, 190, 70, 70))

        if game.game_over == True:
            screen.blit(game_over_surface, (475, 490, 70, 70))

        pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 20)
        screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
        pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 20)
        game.draw(screen)
        pygame.display.update()
        clock.tick(60)




# https://www.youtube.com/watch?v=nF_crEtmpBo