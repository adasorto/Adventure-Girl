import pygame
from constantes import *
from plataforma import *
from utility import Utility
from nivelBase import NivelBase
from enemigo import Enemigo
from fondos import Fondos


class NivelTres(NivelBase):
    '''
    Contiene el diseño del primer nivel.

    '''

    def __init__(self, jugador):
        '''
        Constructor.

        Inicializa los valores para el nivel.

        '''
        NivelBase.__init__(self, jugador)

        # Acceder a las funciones utilitarias
        self.utility = Utility()

        self.nivel = 'Nivel 3'

        # Fondo para el nivel
        self.fondo = self.utility.CargarImagen('bg-nivel-3.png', -1)
        #self.colorFondo = AZULNIVEL3

        # Limite en pixeles del nivel
        self.limiteNivel = -2500

        # Crear las plataformas
        plataformas = [[GRAMAIZQ, 310, 500],
                       [GRAMACEN, 438, 500],
                       [GRAMACEN, 566, 500],
                       [GRAMACEN, 694, 500],
                       [GRAMACEN, 814, 500],
                       [GRAMACEN, 822, 500],
                       [GRAMACEN, 950, 500],
                       [GRAMACEN, 1078, 500],
                       [GRAMACEN, 1206, 500],
                       [GRAMACEN, 1334, 500],
                       [GRAMACEN, 1462, 500],
                       [GRAMACEN, 1590, 500],
                       [PWOODBOX, 1784, 394], # Columna de Cajas Inicio Lado Izquierdo
                       [PWOODBOX, 1890, 394],
                       [PWOODBOX, 1890, 288],
                       [PWOODBOX, 1996, 288],
                       [PWOODBOX, 1996, 182],
                       [PWOODBOX, 1996, 394], # Columna de Cajas Final Lado Izquierdo
                       [GRAMACEN, 1718, 500],
                       [GRAMACEN, 1846, 500],
                       [GRAMACEN, 1974, 500],
                       [GRAMACEN, 2486, 500],
                       [PWOODBOX, 2486, 394], # Columnas de Cajas Inicio Lado Derecho
                       [PWOODBOX, 2486, 288],
                       [PWOODBOX, 2486, 182],
                       [PWOODBOX, 2592, 394],
                       [PWOODBOX, 2592, 288],
                       [PWOODBOX, 2698, 394], # Columna de Cajas Final Lado Izquierdo
                       [GRAMACEN, 2614, 500],
                       [GRAMACEN, 2742, 500],
                       [GRAMACEN, 2870, 500],
                       [GRAMACEN, 2998, 500],
                       [GRAMACEN, 3126, 500],
                       [GRAMACEN, 3254, 500],
                       [GRAMACEN, 3382, 500],
                       [GRAMADER, 3510, 500]]

        # Iterar por la lista de plataformas
        # y agregarlas
        for plataforma in plataformas:
            bloque = Plataforma(self.hojaSprite, plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            self.plataformas.add(bloque)

        # Fondos
        self.listaFondos.add(Fondos(427, 225, 'bTree3.png'))
        self.listaFondos.add(Fondos(468, 460, 'bMushroom1.png'))
        self.listaFondos.add(Fondos(865, 460, 'bMushroom1.png'))
        self.listaFondos.add(Fondos(1120, 455, 'Bush3.png'))
        self.listaFondos.add(Fondos(1299, 455, 'Bush3.png'))
        self.listaFondos.add(Fondos(1320, 455, 'Bush3.png'))
        self.listaFondos.add(Fondos(770, 225, 'bTree3.png'))

        self.listaFondos.add(Fondos(756, 446, 'stone.png'))
        self.listaFondos.add(Fondos(770, 199, 'tree-3.png'))
        self.listaFondos.add(Fondos(3690,510, 'next-level.png'))

        # Enemigos
        self.listaEnemigos.add(Enemigo(680, 415, 'evil-rock-1.png'))
        self.listaEnemigos.add(Enemigo(1526, 415, 'evil-bug-2.png'))
        self.listaEnemigos.add(Enemigo(2102, 500, 'water.png'))
        self.listaEnemigos.add(Enemigo(2230, 500, 'water.png'))
        self.listaEnemigos.add(Enemigo(2358, 500, 'water.png'))
        self.listaEnemigos.add(Enemigo(3100, 415, 'evil-1.png'))
