import pygame

pygame.init()
screen = pygame.display.set_mode((720, 500))
running = True

blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)


clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.QUIT:
            running = False
    pygame.draw.rect(screen, green, [200, 150, 10, 10])
    pygame.display.update()
    clock.tick(50)
pygame.quit()
