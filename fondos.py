import pygame
from utility import Utility
from constantes import *


class Fondos(pygame.sprite.Sprite):
    '''
    Esta clase se encarga de representar todas las imagnes de 
    fondo que decoran en juego.

    '''

    def __init__(self, x, y, fondos):
        '''
        Constructor.

        Inicializa los valores del jugador.

        Parámetros:
        x --> La coordenada en x en pixeles.
        y --> La coordenada en y en pixeles.

        '''
        # Llamar al constructor de la clase padre
        super().__init__()

        # Nuevo objeto de tipo Utility, utilizado
        # para la carga de imágenes
        self.utility = Utility()

        # Dirección hacia la que vé el jugador
        self.direccion = None

        # Obtener todas las imágenes hacia la derecha
        image = self.utility.CargarImagen(fondos)
        self.image = pygame.transform.flip(image, True, False)
        
        # Establecemos una referencia rectangular de la superficie
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
