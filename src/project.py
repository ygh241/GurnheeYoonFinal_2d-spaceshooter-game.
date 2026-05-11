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
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("Space Shooter: Final Project")
    clock = pygame.time.Clock()

    player_img = pygame.image.load("spaceship.png").convert_alpha()
    enemy_img = pygame.image.load("enemy.png").convert_alpha()
    enemy_img = pygame.transform.scale(enemy_img, (60, 60))
    background_img = pygame.image.load("Background_space.png").convert()
    background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

    player = pygame.Rect(WIDTH//2, HEIGHT-60, 50, 40)
    bullets = []
    enemies = [] 
    game_over = False
    score = 0
    running = True

    while running:
        screen.blit(background_img, (0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                # While game is on progress...
                if event.key == pygame.K_ESCAPE: 
                    running = False
                if not game_over:
                    if event.key == pygame.K_SPACE:
                        bullets.append(pygame.Rect(player.centerx - 2, player.top, 4, 10))
                #press R key to restart
                else:
                    if event.key == pygame.K_r:
                        player.x = WIDTH//2
                        bullets = []
                        enemies = []
                        score = 0
                        game_over = False

        if not game_over:
            #player movements
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player.left > 0: player.x -= 7
            if keys[pygame.K_RIGHT] and player.right < WIDTH: player.x += 7

            update_bullets(bullets)
            spawn_enemies(enemies)
            
            #check collision to decide game is over or not
            score, game_over = check_collisions(player, bullets, enemies, score)

            # draw player, bullets, and enemy
            screen.blit(player_img, (player.x, player.y))
            for b in bullets: pygame.draw.rect(screen, WHITE, b)
            for e in enemies: screen.blit(enemy_img, (e.x, e.y))
        else:
            # draw game over screen
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", True, WHITE)
            retry_text = pygame.font.Font(None, 36).render("Press 'R' to Retry", True, WHITE)
            
            screen.blit(text, (WIDTH//2 - 150, HEIGHT//2 - 50))
            screen.blit(retry_text, (WIDTH//2 - 100, HEIGHT//2 + 50))

        #show the score
        font_score = pygame.font.Font(None, 36)
        score_display = font_score.render(f"Score: {score}", True, WHITE)
        screen.blit(score_display, (10, 10))
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

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
            return score, True

    return score, False

if __name__ == "__main__":
    main()