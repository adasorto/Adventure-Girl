import pygame
from utility import Utility

# Constantes
# Éstas definen los tipos de plataformas
# (x, y, ancho, alto)
# x --> Localización en el sprite
# y --> Localización en el sprite
# ancho --> La anchura del sprite
# alto --> Altura del sprite

# Grama Flotante 
PGRAMAIZ = (129, 385, 128, 128)
PGRAMACE = (257, 385, 128, 128)
PGRAMADE = (385, 385, 126, 128)

# Grama Recortada suelo
RGRAMAIZ = (126, 0, 128, 54)
RGRAMACE = (254, 0, 128, 54)
RGRAMADE = (382, 0, 128, 54)

# Grama Recortada Flotante
PRGRAMAIZ = (129, 385, 128, 54)
PRGRAMACE = (257, 385, 128, 54)
PRGRAMADE = (385, 385, 126, 54)

# Grama unida al suelo
GRAMAIZQ = (126, 0, 128, 128)
GRAMACEN = (254, 0, 128, 128)
GRAMADER = (382, 0, 128, 128)
PWOODBOX = (765, 33, 106, 106)
PIEDRACEN = (766, 442, 128, 76)





class Plataforma(pygame.sprite.Sprite):
    '''
    Esta clase representa una pared que limita el movimiento
    del Jugador en pantalla.

    '''

    def __init__(self, hojaSprite, posicion):
        '''
        Constructor.

        Inicializa los valores de una Pared.

        Parámetros:
        hojaSprite --> La imagen conteniendo los sprites
                       a utilizar.

        '''
        # Llama al constructor padre
        super().__init__()

        self.utility = Utility()

        self.image = self.utility.ObtenerImagen(hojaSprite, posicion[0],
                                                posicion[1], posicion[2],
                                                posicion[3])


        self.rect = self.image.get_rect()

