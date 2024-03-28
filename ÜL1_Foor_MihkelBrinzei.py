import pygame
pygame.init() # pygamei alustamine

screen=pygame.display.set_mode([300,300]) # Teeb akna suuruseks 300x300 pikslit
screen.fill([0, 0, 0]) # Taust läheb mustaks
pygame.display.set_caption("Foor - Mihkel Brinzei") # Akna pealkiri

pygame.draw.rect(screen, [179, 179, 179], [95, 35, 110, 210], 0) # Loob halli ristküliku
pygame.draw.rect(screen, [51, 51, 51], [100, 40, 100, 200], 0) # Loob musta ristküliku
pygame.draw.circle(screen, [204, 41, 0], [150, 80], 28, 0) # Loob punase ringi ristkülikute keskele
pygame.draw.circle(screen, [255, 153, 0], [150, 140], 28, 0) # Loob oranži ringi keskele
pygame.draw.circle(screen, [51, 204, 51], [150, 200], 28, 0) # Loob rohelise ringi keskele



pygame.display.flip() # Uuendab ekraani, et näidata joonistust

running = True
while running:
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            pygame.quit() # sulgeb akna kui vajutada ristist
             

