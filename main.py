# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable  = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()

    asteroids  = pygame.sprite.Group()
    
    shots  = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, (0,0,0))

        for to_draw in drawable:
            to_draw.draw(screen)
        updatable.update(dt)

        for object in asteroids:
            is_collision = object.checkColission(player)
            if is_collision == True:
                print("Game over!")
                sys.exit()
            else:
                pass

        for asteroid_col in asteroids:
            for bullet_col in shots:
                is_collision_ast = bullet_col.checkColission(asteroid_col)
                if is_collision_ast == True:
                    asteroid_col.split()
                    bullet_col.kill()
                else:
                    pass

        pygame.display.flip()

        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()
