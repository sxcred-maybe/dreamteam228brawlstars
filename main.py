import pygame

size = width, height = 500, 500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60
x_start, y_start = 250, 250
x, y = x_start, y_start
running = True
while running:
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, 'red', (x_start, y_start), 20)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            per = True
            x, y = event.pos[0], event.pos[1]
        if event.type == pygame.QUIT:
            running = False
    if x > x_start:
        x_start += 1
    elif x < x_start:
        x_start -= 1
    if y > y_start:
        y_start += 1
    elif y < y_start:
        y_start -= 1
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
