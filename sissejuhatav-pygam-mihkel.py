import pygame
pygame.init() # pygamei alustamine

screen=pygame.display.set_mode([640,480]) # Teeb akna suuruseks 300x300 pikslit
screen.fill([204, 255, 255]) # Taust läheb siniseks

pygame.draw.line(screen, [255,0,55], [120,100], [200,243], 2) # joon

pygame.draw.rect(screen, [0, 225, 0], [300, 100, 200, 300], 2) # ristkülik

pygame.draw.circle(screen, [0, 0, 255], [300, 200], 69, 1) # ring

pygame.draw.polygon(screen, [255, 0, 255], [[50,50],[100,50],[40,250],[500,80],[350,250],[50,250]], 2) #hulk nurk

pygame.draw.ellipse(screen, [0, 225, 0], [140, 90, 200, 540], 2) # ovaal

pygame.draw.arc(screen,[55,125,125], [100,100,250,200], 0, 3.14*2, 1) # kaar

pygame.display.flip() # Uuendab ekraani, et näidata joonistust

running = True
while running:
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            pygame.quit() # sulgeb akna kui vajutada ristist
            
#mihkel brinzei