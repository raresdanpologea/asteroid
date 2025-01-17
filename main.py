# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
Player.containers = (updatable, drawable)

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    dt = 0

    print(updatable)
    print(drawable)
    print(Player.containers)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, "black")

        for thing in updatable:
            thing.update(dt)

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
