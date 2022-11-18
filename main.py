import pygame

pygame.init()

# pygame.display.set_mode((600, 400), pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.FULLSCREEN)
sc = pygame.display.set_mode((600, 400))
pygame.display.set_caption("First_app")
# pygame.display.set_icon(pygame.image("app.bmp"))

clock = pygame.time.Clock()  # 60 FPS
FPS = 60

WHITE = (255, 255, 255)
pygame.draw.rect(sc, WHITE, (10, 10, 50, 100), 2)
pygame.display.update()

gm_run = True
# gm_run = True
while gm_run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            gm_run = False

    clock.tick(FPS)
