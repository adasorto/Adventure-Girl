# Cargar lo necesario para el funcionamiento del juego
import pygame
from constantes import *
from plataforma import *
from utility import Utility
from nivelBase import NivelBase
from enemigo import Enemigo
from fondos import Fondos


class NivelUno(NivelBase):
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

        self.nivel = 'Nivel 1'

        # Fondo para el nivel
        self.fondo = self.utility.CargarImagen('bg-nivel-1.png', -1, -1)
        self.colorFondo = NEGRO

        # Limite en pixeles del nivel
        self.limiteNivel = -3000

        # Crear las plataformas
        plataformas = [[GRAMAIZQ, 310, 500],
                       [GRAMACEN, 438, 500],
                       [GRAMACEN, 566, 500],
                       [GRAMACEN, 694, 500],
                       [GRAMACEN, 814, 500],
                       [GRAMACEN, 822, 500],
                       [GRAMACEN, 1078, 500],
                       [GRAMACEN, 1206, 500],
                       [GRAMACEN, 1334, 500],
                       [GRAMACEN, 1718, 500],
                       [GRAMACEN, 1846, 500],
                       [GRAMACEN, 1974, 500],
                       [GRAMACEN, 2102, 500],
                       [PWOODBOX, 2102, 392],
                       [PGRAMAIZ, 2358, 300],
                       [PGRAMACE, 2486, 300],
                       [PGRAMADE, 2614, 300],
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
        self.listaFondos.add(Fondos(756, 455, 'bTree1.png'))
        self.listaFondos.add(Fondos(1150, 240, 'bTree2.png'))
        self.listaFondos.add(Fondos(450, 413, 'Tree_2.png'))
        self.listaFondos.add(Fondos(530, 460, 'bMushroom1.png'))
        self.listaFondos.add(Fondos(1290, 460, 'bMushroom1.png'))
        self.listaFondos.add(Fondos(2460, 260, 'bMushroom1.png'))
        self.listaFondos.add(Fondos(1120, 435, 'Bush1.png'))
        self.listaFondos.add(Fondos(1330,435, 'Bush1.png'))
        self.listaFondos.add(Fondos(3110, 225, 'bTree3.png'))
        self.listaFondos.add(Fondos(3150, 455, 'Bush3.png'))
        self.listaFondos.add(Fondos(3105, 600, 'Bush1.png'))

        self.listaFondos.add(Fondos(756, 455, 'trunk.png'))
        self.listaFondos.add(Fondos(1150, 240, 'tree-1.png'))
        self.listaFondos.add(Fondos(3700,510, 'next-level.png'))
        self.listaFondos.add(Fondos(3150, 455, 'bush-2.png'))
        self.listaFondos.add(Fondos(3105, 600, 'bush-1.png'))

    
        self.listaEnemigos.add(Enemigo(2000, 415, 'evil-bug-1.png'))
        self.listaEnemigos.add(Enemigo(950, 500, 'water.png'))
        self.listaEnemigos.add(Enemigo(2230, 500, 'water.png'))
        self.listaEnemigos.add(Enemigo(2358, 500, 'water.png'))
        self.listaEnemigos.add(Enemigo(2486, 500, 'water.png'))
        self.listaEnemigos.add(Enemigo(2614, 500, 'water.png'))
        self.listaEnemigos.add(Enemigo(2742, 500, 'water.png'))
        self.listaEnemigos.add(Enemigo(1462, 500, 'water.png'))
        self.listaEnemigos.add(Enemigo(1590, 500, 'water.png'))
        self.listaEnemigos.add(Enemigo(3400, 415, 'barrel-flame.png'))


       
