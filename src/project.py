import pygame
import random
import sys

#set the screen size
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Shooter: Step 3")
    clock = pygame.time.Clock()

    player = pygame.Rect(WIDTH//2, HEIGHT-60, 50, 40)
    bullets = []
    enemies = [] 
    running = True

    while running:
        screen.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append(pygame.Rect(player.centerx - 2, player.top, 4, 10))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.left > 0: player.x -= 7
        if keys[pygame.K_RIGHT] and player.right < WIDTH: player.x += 7

        
        update_bullets(bullets)
        spawn_enemies(enemies)
        

        # draw
        pygame.draw.rect(screen, GREEN, player)
        for b in bullets: 
            pygame.draw.rect(screen, WHITE, b)
        for e in enemies:
            pygame.draw.rect(screen, RED, e) #draw enemy
        
        pygame.display.flip()
        clock.tick(60)

def update_bullets(bullets):
    for b in bullets[:]:
        b.y -= 10
        if b.bottom < 0:
            bullets.remove(b)

def spawn_enemies(enemies):
    """Function 2: Handles randomized enemy spawning"""
    if random.random() < 0.03: # 3 percentage of make it random
        new_enemy = pygame.Rect(random.randint(0, WIDTH-40), -40, 40, 40)
        enemies.append(new_enemy)
    
    for e in enemies[:]:
        e.y += 4
        if e.top > HEIGHT:
            enemies.remove(e)

if __name__ == "__main__":
    main()