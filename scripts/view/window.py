import pygame
import sys

# Inizializza pygame
pygame.init()

# Imposta dimensioni della finestra
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Imposta il titolo della finestra
pygame.display.set_caption("I-kant")

# Loop principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Riempie lo sfondo
    screen.fill((0, 0, 0))

    # Aggiorna la finestra
    pygame.display.flip()

# Esce da pygame
pygame.quit()
sys.exit()