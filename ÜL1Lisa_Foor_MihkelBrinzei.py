import pygame
pygame.init() # pygamei alustamine

screen=pygame.display.set_mode([300,300]) # Teeb akna suuruseks 300x300 pikslit
screen.fill([0, 0, 0]) # Taust läheb mustaks
pygame.display.set_caption("Foor - Mihkel Brinzei") # Akna pealkiri

pygame.draw.line(screen, [179,179,179], [150,100], [150,260], 5) # Loob halli joone - post

pygame.draw.polygon(screen, [255, 255, 255], [[190,300],[110,300],[120,290],[180,290]], 0) # Hulknurga tegemine - Eesti lipu värvid
pygame.draw.polygon(screen, [0, 153, 255], [[150,260],[135,278],[165,278]], 0) # Sinine värv


pygame.draw.line(screen, [179,179,179], [150,260], [110,300], 5) # Loob hallid jooned - posti vasak alus
pygame.draw.line(screen, [179,179,179], [150,260], [190,300], 5) # Parem posti alus
pygame.draw.line(screen, [179,179,179], [190,300], [110,300], 5) # Alus


pygame.draw.rect(screen, [179, 179, 179], [95, 35, 110, 210], 0) # Loob halli ristküliku !!FOOR PEA OSA!!
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
             

