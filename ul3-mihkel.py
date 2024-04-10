# Mihkel Brinzei

import pygame
pygame.init()

# Värvid
red = [255, 0, 0]
lGreen = [153, 255, 153]
blue = [0, 0, 255]
pink = [255, 153, 255]

# Ekraani seaded
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Ülesanne 3 - Mihkel Brinzei")
screen.fill(lGreen)

paksus = 1

# Funktsioon
def drawJoon(ridade_arv, veergude_arv, color, paksus): # defineerib mida kasutada saab
    x_veerg = 640 / veergude_arv #arvutab välja kui kaugel on järgmine veerg/ rida
    y_rida = 480 / ridade_arv #arvutab välja kui kaugle on rida

    for i in range(veergude_arv): # tsükkel veergude jaoks
        x = i * x_veerg # arvutab välja kui palju vahet jätta 8 x 80
        pygame.draw.line(screen, color, [x, 0], [x, 480], paksus) # joonistab joone 8 korda 80 pikslise vahega
    
    for j in range(ridade_arv): # tsükkel ridade jaoks
        y = j * y_rida # arvutab kui palju vahet jätte 8 x 80
        pygame.draw.line(screen, color, [0, y], [640, y], paksus) # joonistab 8x 80 pikslise vahega

    pygame.display.flip() # uuendab ekraani

drawJoon(10, 10, red, paksus)  # Joonistab 5 rida ja 5 veergu

running = True # tükk koodi mis laseb ekraani X'st kinni panna
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()  # Sulgeb akna, kui vajutatakse ristist