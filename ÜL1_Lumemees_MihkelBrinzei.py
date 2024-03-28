import pygame
pygame.init() # pygamei alustamine

screen=pygame.display.set_mode([300,300]) # Teeb akna suuruseks 300x300 pikslit
screen.fill([0, 0, 0]) # Taust läheb mustaks
pygame.display.set_caption("Lumemees - Mihkel Brinzei") # Akna pealkiri

pygame.draw.circle(screen, [255, 255, 255], [150, 225], 50, 0) # Loob valged ringid - keha
pygame.draw.circle(screen, [255, 255, 255], [150, 140], 40, 0)
pygame.draw.circle(screen, [255, 255, 255], [150, 75], 30, 0)

pygame.draw.circle(screen, [0, 0, 0], [140, 70], 5, 0) # Loob mustad ringid - silmad
pygame.draw.circle(screen, [0, 0, 0], [160, 70], 5, 0)

pygame.draw.polygon(screen, [255, 153, 0], [[145,80],[155,80],[155,80],[150,95],[145,80],[150,95]], 0) # Oranži hulknurga tegemine - nina

pygame.display.flip() # Uuendab ekraani, et näidata joonistust

running = True
while running:
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            pygame.quit() # sulgeb akna kui vajutada ristist