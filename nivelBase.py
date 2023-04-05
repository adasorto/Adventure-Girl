import pygame
from constantes import *
from plataforma import Plataforma
from utility import Utility


class NivelBase(object):
    '''
    Clase en la que se basan todos los niveles del juego.

    '''

    listaParedes = None
    listaEnemigos = None
    listaFondos = None

    def __init__(self, jugador):
        '''
        Constructor.

        Inicializa el objeto NivelBase.

        '''
        self.utility = Utility()
        self.plataformas = pygame.sprite.Group()
        self.listaEnemigos = pygame.sprite.Group()
        self.listaFondos = pygame.sprite.Group()
        self.jugador = jugador
        self.desplazamiento = 0
        self.hojaSprite = 'Tile.png'
        self.fondo = None
        self.colorFondo = NEGRO
        self.reloj = pygame.time.get_ticks()
        self.cuenta = 3
        self.intro = True
        self.pausa = 1000
        self.nivel = 0

    def update(self):
        '''
        Actualizar todo el nivel.

        '''
        self.plataformas.update()
        self.listaEnemigos.update()
        self.listaFondos.update()

    def Dibujar(self, pantalla):
        '''
        Dibujar todos los objetos del nivel en la superficie.

        Parámetros:
        pantalla --> La superficie sobre la que se dibuja el nivel.

        '''
    
        pantalla.fill(self.colorFondo)
        pantalla.blit(self.fondo, (self.desplazamiento // 3, 0))

        # Dibujar todos los sprites
        self.plataformas.draw(pantalla)
        self.listaEnemigos.draw(pantalla)
        self.listaFondos.draw(pantalla)

    def Desplazar(self, desplazarX):
        '''
        Reliza el movimiento del escenario cuando el jugador se
        aproxima a los límites de la superficie.

        Parámetros:
        pantalla --> La superficie que contiene los límites.

        '''
        # Llevamos la cuenta de la cantidad de pixeles que se
        # debería de desplazar el nivel
        self.desplazamiento += desplazarX

        # Iteramos a través de todas las listas de sprites y
        # desplazamos la cantidad de pixeles necesarias
        for plataforma in self.plataformas:
            plataforma.rect.x += desplazarX

        for enemigo in self.listaEnemigos:
            enemigo.rect.x += desplazarX

        for fondos in self.listaFondos:
            fondos.rect.x += desplazarX

    def Introduccion(self, pantalla):
        '''
        Despliega un contador al inicio de cada nivel.
        self.cuenta lleva la cuenta del tiempo a contar
        de más a menos.

        Parámetros:
        pantalla --> La superficie sobre la que se dibujará.

        '''


        # Realizar un conteo desde self.cuenta hasta cero.
        
        while self.cuenta >= 0:
            # Colocamos el color de fondo
            pantalla.fill(self.colorFondo)
            pantalla.blit(self.fondo, (self.desplazamiento // 3, 0))
            # Obtener el tiempo actual
            now = pygame.time.get_ticks()
            # Si el tiempo actual menos el tiempo inicial
            # tomado al construir el objeto es mayor que
            # nuestro tiempo de pausa en milisegundos
            # mostrar el tiempo de contador y restarle uno.
            if now - self.reloj > self.pausa:
                self.reloj = now
                if self.cuenta > 0:
                    self.utility.MostrarTexto(self.nivel, 70, 'verdana',
                                              BLANCO, [290, 150],
                                              pantalla, False)
                    self.utility.MostrarTexto(str(self.cuenta), 80, 'consolas',
                                              NEGRO, [0, 0], pantalla)
                    pygame.display.flip()

                self.cuenta -= 1

        self.intro = False
        
