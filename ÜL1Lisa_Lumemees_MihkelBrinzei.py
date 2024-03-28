import pygame
pygame.init() # pygamei alustamine

screen=pygame.display.set_mode([300,300]) # Teeb akna suuruseks 300x300 pikslit
screen.fill([204, 255, 255]) # Taust läheb siniseks
pygame.display.set_caption("Lumemees - Mihkel Brinzei") # Akna pealkiri

pygame.draw.circle(screen, [255,255,0], [300,0], 75, 0) # tekitab kollased jooned ja ringid - päike
pygame.draw.line(screen, [255,255,0], [300,0], [0,280], 4)
pygame.draw.line(screen, [255,255,0], [300,0], [0,20], 4)
pygame.draw.line(screen, [255,255,0], [300,0], [280,300], 4)
pygame.draw.line(screen, [255,255,0], [300,0], [0,150], 4)
pygame.draw.line(screen, [255,255,0], [300,0], [150,300], 4)

pygame.draw.circle(screen, [255, 255, 255], [20,40], 18, 0) # tekitab valged ringid - pilv 1
pygame.draw.circle(screen, [255, 255, 255], [40,30], 20, 0)
pygame.draw.circle(screen, [255, 255, 255], [60,40], 18, 0)

pygame.draw.circle(screen, [255, 255, 255], [200,60], 18, 0) # tekitab valged ringid - pilv 2
pygame.draw.circle(screen, [255, 255, 255], [220,50], 20, 0)
pygame.draw.circle(screen, [255, 255, 255], [240,60], 18, 0)

pygame.draw.circle(screen, [255, 255, 255], [30,150], 18, 0) # tekitab valged ringid - pilv 3
pygame.draw.circle(screen, [255, 255, 255], [50,140], 20, 0)
pygame.draw.circle(screen, [255, 255, 255], [70,150], 18, 0)

pygame.draw.circle(screen, [255, 255, 255], [150, 225], 50, 0) # Loob valged ringid - keha
pygame.draw.circle(screen, [255, 255, 255], [150, 140], 40, 0)
pygame.draw.circle(screen, [255, 255, 255], [150, 75], 30, 0)

pygame.draw.line(screen, [0,0,0], [80,80], [80,200], 4) # Joonistab musta joone - hari
pygame.draw.line(screen, [128,128,128], [80,80], [65,40], 4)
pygame.draw.line(screen, [128,128,128], [80,80], [50,40], 4)
pygame.draw.line(screen, [128,128,128], [80,80], [95,40], 4)
pygame.draw.line(screen, [128,128,128], [80,80], [110,40], 4)
pygame.draw.line(screen, [128,128,128], [80,80], [80,40], 4) # keskmine pulk
pygame.draw.line(screen, [128,128,128], [80,80], [103,40], 4)
pygame.draw.line(screen, [128,128,128], [80,80], [57,40], 4)
pygame.draw.line(screen, [128,128,128], [80,80], [87,40], 4)
pygame.draw.line(screen, [128,128,128], [80,80], [73,40], 4)


pygame.draw.line(screen, [128,77,0], [80,100], [120,120], 4) # Joonistab pruunid jooned - käed
pygame.draw.line(screen, [128,77,0], [240,100], [180,120], 4)

pygame.draw.circle(screen, [0, 0, 0], [150, 140], 5, 0) # Loob mustad ringid - nööbid
pygame.draw.circle(screen, [0, 0, 0], [150, 180], 5, 0)  
pygame.draw.circle(screen, [0, 0, 0], [150, 225], 5, 0)


pygame.draw.line(screen, [0,0,0], [120,55], [180,55], 4) # müts
pygame.draw.rect(screen, [0,0,0], [130, 25, 40, 30], 0) 



pygame.draw.circle(screen, [0, 0, 0], [140, 70], 5, 0) # Loob mustad ringid - silmad
pygame.draw.circle(screen, [0, 0, 0], [160, 70], 5, 0)

pygame.draw.polygon(screen, [255, 153, 0], [[145,80],[155,80],[155,80],[150,95],[145,80],[150,95]], 0) # Oranži hulknurga tegemine - nina

pygame.display.flip() # Uuendab ekraani, et näidata joonistust

running = True
while running:
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            pygame.quit() # sulgeb akna kui vajutada ristist        