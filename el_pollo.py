import pygame
import random
import sys

pygame.init()

ANCHO = 600
ALTO = 800
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Evita los obstáculos")

rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (0,255,0)
rosado = (255,192,203)
negro = (0,0,0)
amarillo = (255,255,0)
blanco = (255,255,255)
Naranja = (255,165,0)
cian = ( 0,255,255)
gris = (128,128,128)

autos1 = 0
autos2 = 600
autos3 = 0
autos4 = 600
derecha = 2
izquierda = -2
derecha2 = 4
izquierda2 = -4
autos5 = 700
autos6 = 700
autos7 = 700
autos8 = 700


XX1 = 290
YY1 = 750
jugador_rect = pygame.Rect(XX1, YY1, 40, 40)


clock = pygame.time.Clock()
FPS = 60


vidas = 1
fuente = pygame.font.SysFont(None, 36)

def mostrar_vidas():
    texto = fuente.render(f"vidas: {vidas}", True, blanco)
    ventana.blit(texto, (10, 10))


def verificar_colision(rect1, rect2):
    return rect1.colliderect(rect2)


frame_count = 0
jugando = True
while jugando:
    clock.tick(FPS)
    ventana.fill(verde)
    autos1 = autos1 + derecha
    autos2 = autos2 + izquierda
    autos3 = autos3 + derecha
    autos4 = autos4 + izquierda2
    autos5 = autos5 + izquierda2
    autos6 = autos6 + izquierda2
    autos7 = autos6 + derecha2
    autos7 = autos7 + izquierda2

    if autos1 >= 500:
        autos1 = 0

    if autos2 <= 50:
        autos2 = 600

    if autos3 >= 420:
        autos3 = 0

    if autos4 <= 0:
        autos4 = 600

    if autos5 <= 0:
        autos5 = 600

    if autos6 <= 0:
        autos6 = 600


    pygame.draw.rect(ventana, gris, (1,200, 600,100))
    pygame.draw.rect(ventana, gris, (1,430, 600,100))
    pygame.draw.rect(ventana, negro, (1,220, 600,290))
    keys = pygame.key.get_pressed()  
    if keys[pygame.K_w]:  # Tecla W (arriba)
        YY1 -= 3
    if keys[pygame.K_s]:  # Tecla S (abajo)
        YY1 += 3
    if keys[pygame.K_a]:  # Tecla A (izquierda)
        XX1 -= 3
    if keys[pygame.K_d]:  # Tecla D (derecha)
        XX1 += 3

    
    jugador_rect.topleft = (XX1, YY1)

    obstaculo_rojo1 = pygame.Rect(5, 100, 100, 100)
    obstaculo_rojo2 = pygame.Rect(150, 100, 100, 100)
    obstaculo_rojo3 = pygame.Rect(300, 100, 100, 100)
    obstaculo_rojo4 = pygame.Rect(5, 550, 100, 100)
    obstaculo_rojo5 = pygame.Rect(150, 550, 100, 100)
    obstaculo_cian1 = pygame.Rect(autos2, 460, 40, 30)
    obstaculo_naranja1 = pygame.Rect(autos4, 400, 40, 30)
    obstaculo_rosado1 = pygame.Rect(autos3, 460, 40, 30)
    obstaculo_verde1 = pygame.Rect(autos1, 470, 40, 30)
    obstaculo_blanco1 = pygame.Rect(autos4, 470, 40, 30)
    obstaculo_gris1 = pygame.Rect(autos3, 400, 40, 30)
    obstaculo_amarillo1 = pygame.Rect(autos1, 470, 40, 30)
    obstaculo_cian2 = pygame.Rect(autos2, 270, 40, 30)
    obstaculo_naranja2 = pygame.Rect(autos4, 300, 40, 30)
    obstaculo_verde2 = pygame.Rect(autos1, 250, 40, 30)
    obstaculo_blanco2 = pygame.Rect(autos4, 210, 40, 30)
    obstaculo_gris2 = pygame.Rect(autos3, 260, 40, 30)
    obstaculo_amarillo2 = pygame.Rect(autos1, 310, 40, 30)

    pygame.draw.rect(ventana, rojo, obstaculo_rojo1)
    pygame.draw.rect(ventana, rojo, obstaculo_rojo2)
    pygame.draw.rect(ventana, rojo, obstaculo_rojo3)
    pygame.draw.rect(ventana, rojo, obstaculo_rojo4)
    pygame.draw.rect(ventana, rojo, obstaculo_rojo5)
    pygame.draw.rect(ventana, negro, (140,530,120,30))
    pygame.draw.rect(ventana, negro, (1,530,120,30))
    pygame.draw.rect(ventana, negro, (1,100,120,30))
    pygame.draw.rect(ventana, negro, (140,100,120,30))
    pygame.draw.rect(ventana, negro, (290,100,120,30))
    pygame.draw.rect(ventana, verde, (1,340, 600,50))
    
    pygame.draw.rect(ventana, Naranja, obstaculo_naranja1)
    pygame.draw.rect(ventana, rosado, obstaculo_rosado1)
    pygame.draw.rect(ventana, verde, obstaculo_verde1)
    pygame.draw.rect(ventana, blanco, obstaculo_blanco1)
    pygame.draw.rect(ventana, gris, obstaculo_gris1)
    pygame.draw.rect(ventana, amarillo, obstaculo_amarillo1)
    
    
    pygame.draw.rect(ventana, Naranja, obstaculo_naranja2)
    pygame.draw.rect(ventana, verde, obstaculo_verde2)
    pygame.draw.rect(ventana, blanco, obstaculo_blanco2)
    pygame.draw.rect(ventana, gris, obstaculo_gris2)
    pygame.draw.rect(ventana, amarillo, obstaculo_amarillo2)
    pygame.draw.rect(ventana, amarillo, jugador_rect)  


    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    


    
    if verificar_colision(jugador_rect, obstaculo_rojo1) or \
       verificar_colision(jugador_rect, obstaculo_rojo2) or \
       verificar_colision(jugador_rect, obstaculo_rojo3) or \
       verificar_colision(jugador_rect, obstaculo_rojo4) or \
       verificar_colision(jugador_rect, obstaculo_rojo5) or \
       verificar_colision(jugador_rect, obstaculo_cian1) or \
       verificar_colision(jugador_rect, obstaculo_naranja1) or \
       verificar_colision(jugador_rect, obstaculo_rosado1) or \
       verificar_colision(jugador_rect, obstaculo_verde1) or \
       verificar_colision(jugador_rect, obstaculo_blanco1) or \
       verificar_colision(jugador_rect, obstaculo_gris1) or \
       verificar_colision(jugador_rect, obstaculo_amarillo1) or \
       verificar_colision(jugador_rect, obstaculo_cian2) or \
       verificar_colision(jugador_rect, obstaculo_naranja2) or \
       verificar_colision(jugador_rect, obstaculo_verde2) or \
       verificar_colision(jugador_rect, obstaculo_blanco2) or \
       verificar_colision(jugador_rect, obstaculo_gris2) or \
       verificar_colision(jugador_rect, obstaculo_amarillo2):
        vidas -= 1
        print("¡Colisión! Vidas:", vidas)
        
    
        if vidas <= 0:
            jugando = False

    
    mostrar_vidas()

    
    pygame.display.flip()
    frame_count += 1


pygame.quit()
sys.exit()
