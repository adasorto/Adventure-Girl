import pygame
from constantes import *
from plataforma import *
from utility import Utility
from nivelBase import NivelBase
from enemigo import Enemigo
from fondos import Fondos


class NivelDos(NivelBase):
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

        self.nivel = 'Nivel 2'

        # Fondo para el nivel
        self.fondo = self.utility.CargarImagen('bg-nivel-2.png', -1)
        self.colorFondo = AZULNIVEL2

        # Limite en pixeles del nivel
        self.limiteNivel = -2500

        # Crear las plataformas
        plataformas = [[PGRAMAIZ, 694, 450], # Primera Plataforma
                       [PGRAMACE, 814, 450],
                       [PGRAMADE, 942, 450],
                       [PGRAMAIZ, 1198, 350], # Segunda Plataforma
                       [PGRAMADE, 1326, 350],
                       [PGRAMAIZ, 1718, 250], # Tercera Plataforma
                       [PGRAMACE, 1846, 250],
                       [PGRAMADE, 1974, 250],
                       [PGRAMAIZ, 2230, 150], # Cuarta Plataforma
                       [PGRAMADE, 2358, 150],
                       [PGRAMAIZ, 2742, 250], # Quinta Plataforma
                       [PGRAMACE, 2870, 250],
                       [PGRAMADE, 2998, 250]]

        # Iterar por la lista de plataformas
        # y agregarlas
        for plataforma in plataformas:
            bloque = Plataforma(self.hojaSprite, plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            self.plataformas.add(bloque)

        # Fondos para ser agregados en las palataformas flotantes
        self.listaFondos.add(Fondos(800, 403, 'Bush3.png'))
        self.listaFondos.add(Fondos(785, 175, 'bTree3.png'))
        self.listaFondos.add(Fondos(855, 410, 'bMushroom1.png'))
        self.listaFondos.add(Fondos(800, 403, 'Bush3.png'))
        self.listaFondos.add(Fondos(1375, 309, 'bMushroom1.png'))
        self.listaFondos.add(Fondos(1249, 297, 'Stone.png'))
        self.listaFondos.add(Fondos(1875, 210, 'bMushroom1.png'))
        self.listaFondos.add(Fondos(1840, -25, 'bTree3.png'))
        self.listaFondos.add(Fondos(2760, 163, 'Tree_2.png'))
         

        self.listaFondos.add(Fondos(800, 403, 'bush-2.png'))
        self.listaFondos.add(Fondos(1840, -25, 'tree-2.png'))
        self.listaFondos.add(Fondos(3258,510, 'next-level.png'))

        # Enemigo en este nivel solo sera en agua al caer de una plataforma perdera el jugador
        self.listaEnemigos.add(Enemigo(1078, 430, 'acid.png'))
        self.listaEnemigos.add(Enemigo(1206, 430, 'acid.png'))
        self.listaEnemigos.add(Enemigo(1334, 430, 'acid.png'))
        self.listaEnemigos.add(Enemigo(1462, 430, 'acid.png'))
        self.listaEnemigos.add(Enemigo(1590, 430, 'acid.png'))
        self.listaEnemigos.add(Enemigo(1718, 430, 'acid.png'))
        self.listaEnemigos.add(Enemigo(1830, 165, 'barrel-acid.png'))
        self.listaEnemigos.add(Enemigo(1846, 430, 'acid.png'))
        self.listaEnemigos.add(Enemigo(1974, 430, 'acid.png'))
        self.listaEnemigos.add(Enemigo(2102, 430, 'acid.png'))
        self.listaEnemigos.add(Enemigo(2230, 430, 'acid.png'))
        self.listaEnemigos.add(Enemigo(2358, 430, 'acid.png'))
        self.listaEnemigos.add(Enemigo(2486, 430, 'acid.png'))
        self.listaEnemigos.add(Enemigo(2614, 430, 'acid.png'))
        self.listaEnemigos.add(Enemigo(2742, 430, 'acid.png'))
        self.listaEnemigos.add(Enemigo(2870, 430, 'acid.png'))
        self.listaEnemigos.add(Enemigo(2915, 165, 'evil-bug-3.png'))
        self.listaEnemigos.add(Enemigo(2998, 430, 'acid.png'))
