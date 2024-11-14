import pygame
import random 

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 512
GRID_SIZE = 32
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE  

def main():
    try
        pygame.init()
        mole_pos = (0, 0) 
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Check for mouse clicks
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    mole_rect = mole_image.get_rect(topleft=mole_pos)

                    # Check if the click is on the mole
                    if mole_rect.collidepoint(mouse_x, mouse_y):
                        # Move mole to a random grid position
                        mole_x = random.randrange(GRID_WIDTH) * GRID_SIZE
                        mole_y = random.randrange(GRID_HEIGHT) * GRID_SIZE
                        mole_pos = (mole_x, mole_y)

            # Fill the screen with a background color
            screen.fill("light green")

            # Draw the grid
            for x in range(0, SCREEN_WIDTH, GRID_SIZE):
                pygame.draw.line(screen, "black", (x, 0), (x, SCREEN_HEIGHT))
            for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
                pygame.draw.line(screen, "black", (0, y), (SCREEN_WIDTH, y))

            # Draw the mole at the current position
            screen.blit(mole_image, mole_image.get_rect(topleft=mole_pos))

            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
