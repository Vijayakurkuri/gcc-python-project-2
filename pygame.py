import pygame
import random

# Initialize Pygame
pygame.init()

# Game window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Paddle dimensions
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
PADDLE_SPEED = 10

# Ball dimensions
BALL_RADIUS = 10
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Brick dimensions
BRICK_WIDTH = 80
BRICK_HEIGHT = 20
BRICK_ROWS = 5
BRICK_COLS = 10

# Create the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Brick Breaker")

def draw_paddle(paddle_x):
    pygame.draw.rect(window, GREEN, (paddle_x, WINDOW_HEIGHT - PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT))

def draw_ball(ball_x, ball_y):
    pygame.draw.circle(window, BLUE, (ball_x, ball_y), BALL_RADIUS)

def draw_bricks(bricks):
    for brick in bricks:
        pygame.draw.rect(window, RED, brick)

def brick_breaker_game():
    paddle_x = (WINDOW_WIDTH - PADDLE_WIDTH) // 2
    ball_x, ball_y = WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2
    ball_speed_x = BALL_SPEED_X
    ball_speed_y = BALL_SPEED_Y

    bricks = []
    for row in range(BRICK_ROWS):
        for col in range(BRICK_COLS):
            brick_x = col * (BRICK_WIDTH + 5)
            brick_y = row * (BRICK_HEIGHT + 5)
            bricks.append(pygame.Rect(brick_x, brick_y, BRICK_WIDTH, BRICK_HEIGHT))

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle_x = max(paddle_x - PADDLE_SPEED, 0)
        if keys[pygame.K_RIGHT]:
            paddle_x = min(paddle_x + PADDLE_SPEED, WINDOW_WIDTH - PADDLE_WIDTH)

        ball_x += ball_speed_x
        ball_y += ball_speed_y

        if ball_x <= 0 or ball_x >= WINDOW_WIDTH:
            ball_speed_x = -ball_speed_x

        if ball_y <= 0:
            ball_speed_y = -ball_speed_y

        if ball_y >= WINDOW_HEIGHT:
            pygame.quit()
            return

        # Collision with paddle
        if ball_y >= WINDOW_HEIGHT - PADDLE_HEIGHT - BALL_RADIUS and paddle_x <= ball_x <= paddle_x + PADDLE_WIDTH:
            ball_speed_y = -ball_speed_y

        # Collision with bricks
        for brick in bricks:
            if brick.colliderect(pygame.Rect(ball_x - BALL_RADIUS, ball_y - BALL_RADIUS, 2 * BALL_RADIUS, 2 * BALL_RADIUS)):
                ball_speed_y = -ball_speed_y
                bricks.remove(brick)
                break

        window.fill(BLACK)
        draw_paddle(paddle_x)
        draw_ball(ball_x, ball_y)
        draw_bricks(bricks)
        pygame.display.update()
        clock.tick(100)

if __name__ == "__main_":
    brick_breaker_game()