import pygame, sys
from pygame.locals import *


pygame.init()
#variables del ancho y largo de la pantalla
W = 500
H = 400

PANTALLA =  pygame.display.set_mode((W, H))
#nombre de la ventana
pygame.display.set_caption("espacio")
#cargar al icono
icono = pygame.image.load("imagenes/nave.png")
#llamar al icono
pygame.display.set_icon(icono)
#cargar el fondo
#el.convert es para pasar la imagen del juego a un formato mas eficiente
fondo=pygame.image.load("imagenes/cielo.png").convert()
#reescalar la imagen para que se ajuste
fondo = pygame.transform.scale(fondo, (500, 500))
#x e y son las variables de la posicion en la que esta la imagen
x=0
y=0
#hacer que el fondo se muestre en pantalla 
PANTALLA.blit(fondo,(x,y))

nave_x=400
nave_y=200
nave=pygame.image.load("imagenes/nave.png")
nave = pygame.transform.scale(nave, (100, 100))
PANTALLA.blit(nave,(nave_x,nave_y))





#declarar animaciones y resto de cosas
explosion = [pygame.image.load("imagenes/explosion/explosion1.png"),
pygame.image.load("imagenes/explosion/explosion2.png"),
pygame.image.load("imagenes/explosion/explosion3.png"),
pygame.image.load("imagenes/explosion/explosion4.png"), 
pygame.image.load("imagenes/explosion/explosion5.png"),
pygame.image.load("imagenes/explosion/explosion6.png"),
pygame.image.load("imagenes/explosion/explosion7.png")]

fuego = [pygame.image.load("imagenes/fuego/fuego1.png"),
pygame.image.load("imagenes/fuego/fuego2.png")]

bala = pygame.image.load("imagenes/bala.png")









      

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            #esto se encarga del bucle del fondo
    yRelativa = y % fondo.get_rect().height
    PANTALLA.blit(fondo,(x,yRelativa - fondo.get_rect().height))
    if yRelativa < H:
        PANTALLA.blit(fondo,(x,yRelativa))
    #esto hace que y se reste 3 todo el aro pero escrito abreviado
    y += 3
    PANTALLA.blit(nave,(nave_x,nave_y))

    #acortar codigo, cada vez que ponga key sera que tenga que mantenerse presionada
    keys = pygame.key.get_pressed()
    
        
     #moverme con w
    if keys[pygame.K_d]:
        nave_x = nave_x + 5
    elif keys[pygame.K_a]:
        nave_x = nave_x - 5
    elif keys[pygame.K_w]:
        nave_y = nave_y - 5
    elif keys[pygame.K_s]:
        nave_y = nave_y + 5
   
        
   
    
    pygame.display.update()
  
    pygame.time.Clock().tick(60)