import pygame
from utility import Utility
from constantes import *


class Enemigo(pygame.sprite.Sprite):
    '''
    Esta clase representa al protagonista del juego.

    Se encarga de todas las acciones del enemigo.

    '''

    def __init__(self, x, y, enemigo):
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
        image = self.utility.CargarImagen(enemigo)
        self.image = pygame.transform.flip(image, True, False)

        # Establecemos una referencia rectangular de la superficie
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def Mover(self, direccion):
        '''
        Mueve al enemigo en la plataforma.
        '''
        self.rect.x += direccion

    def update(self):
        '''
        Actualiza el jugador a la posición
        del cursor del mouse en la aplicación.

        '''
        self.Mover(-1)


