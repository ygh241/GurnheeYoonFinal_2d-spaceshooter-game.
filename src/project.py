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

    player_img = pygame.image.load("spaceship.png").convert_alpha()
    enemy_img = pygame.image.load("enemy.png").convert_alpha()
    enemy_img = pygame.transform.scale(enemy_img, (60, 60))
    background_img = pygame.image.load("Background_space.png").convert()
    background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

    player = pygame.Rect(WIDTH//2, HEIGHT-60, 50, 40)
    bullets = []
    enemies = [] 
    score = 0
    running = True

    while running:
        screen.blit(background_img, (0, 0))
        
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
        
        # checking collisions with update
        score = check_collisions(player, bullets, enemies, score)

        # draw

        screen.blit(player_img, (player.x, player.y))

        for b in bullets:
            pygame.draw.rect(screen, WHITE, b)
            
        for e in enemies:
            screen.blit(enemy_img, (e.x, e.y))

        #show the score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        
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
        new_enemy = pygame.Rect(random.randint(0, WIDTH-60), -60, 60, 60)
        enemies.append(new_enemy)
    
    for e in enemies[:]:
        e.y += 4
        if e.top > HEIGHT:
            enemies.remove(e)

    
def check_collisions(player, bullets, enemies, score):
    """Function 3: Handles all collision detection"""
    # Bullets coliding with enemy
    for b in bullets[:]:
        for e in enemies[:]:
            if b.colliderect(e):
                bullets.remove(b)
                enemies.remove(e)
                score += 10 # when the bullets collide with enemy add 10 points
                break
    
    # player coliding with enemy
    for e in enemies:
        if e.colliderect(player):
            print(f"GAME OVER! Final Score: {score}")
            pygame.quit()
            sys.exit()   #when player collide with enemy, automatically quit the window.

    return score

if __name__ == "__main__":
    main()