import pygame

pygame.init()

# Window setup
width = 600
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animated Circle")

# Circle properties
x = 300
y = 300
radius = 30
speed = 5

running = True

while running:

    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
    
    pygame.display.update()

pygame.quit()