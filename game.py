#------------------------Universidad Catolica--------------------------
#--------------------Nuetra Señora Reina de la Paz---------------------
#-----------------------Programa de Cientifica II----------------------
#------------------Catedratico: Ing. Hector Sabillon-------------------
#-----------------Integrante: Ada Jensy Sorto Tinoco-------------------
#----------------------- 18 de Agosto del 2018--------------------------
#----------------------Siguatepeque, Comayagua-------------------------

import pygame
from constantes import *
from nivelUno import NivelUno
from nivelDos import NivelDos
from nivelTres import NivelTres
from jugador import Jugador
from utility import Utility
from pygame.locals import *

# Iniciar el motor de juego
pygame.init()

# Definir la superficie principal
PANTALLA = pygame.display.set_mode(VENTANA)

# Definir el reloj de juego
fpsClock = pygame.time.Clock()


class Game(object):
    '''
    Esta clase representa una instancia del juego

    Se encarga del manejo global de todo lo que
    el juego representa.

    '''

    def __init__(self):
        '''
        Constructor

        Crea todos los objetos e inicializa los atributos
        de nuestro juego.
        '''
        # Se encarga de acceder a funciones utilitarias
        self.utility = Utility()

        self.puntuacion = 0
        self.gameOver = False

        self.nivelSiguiente = False

        self.inicioJuego = False
        self.posicionOpcionY = 400
        self.opcion = 1

        # Crear una lista de sprites
        self.listaSprites = pygame.sprite.Group()
        self.desplazarNiveles = pygame.sprite.Group()

        # Crear nuestro protagonista
        self.jugador = Jugador(50, 50)

        self.fondoNivelCompleto = self.utility.CargarImagen('bg-nivel-superado.png')
        self.fondoNivelCompleto = pygame.transform.scale(self.fondoNivelCompleto, [800,600])

        # Pantalla de Inicio
        self.imgGanar = self.utility.CargarImagen('bg-ganaste.png')
        self.imgGanar = pygame.transform.scale(self.imgGanar, [800,600])
        self.imgPerder = self.utility.CargarImagen('Perdiste.png')
        self.imgPerder = pygame.transform.scale(self.imgPerder, [800,600])

        self.imgMenuPrincipal = self.utility.CargarImagen('bg-inicio.png')
        self.imgMenuPrincipal = pygame.transform.scale(self.imgMenuPrincipal, [800,600])
        self.flecha = self.utility.CargarImagen('flecha.png')
        self.flecha = pygame.transform.scale(self.flecha, [70, 40])

        # Agregar los niveles del juego
        self.niveles = []
        self.niveles.append(NivelUno(self.jugador))
        self.niveles.append(NivelDos(self.jugador))
        self.niveles.append(NivelTres(self.jugador))


        # Nivel inicial
        self.nivelActual = 2

        # Nivel Maximos
        self.nivelMax = len(self.niveles) - 1

        self.jugador.nivel = self.niveles[self.nivelActual]

        self.jugador.rect.x = ANCHO / 4
        self.jugador.rect.y = ALTO - self.jugador.rect.height

        # Agregar el protagonista a lista de los sprites
        self.listaSprites.add(self.jugador)

    def ProcesarEventos(self):
        '''
        Procesar los eventos dentro del juego.

        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

            # El jugador presiona una tecla
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.gameOver:
                        self.__init__()
                if event.key == pygame.K_LEFT:
                    self.jugador.Izquierda()
                if event.key == pygame.K_RIGHT:
                    self.jugador.Derecha()
                if event.key == pygame.K_UP:
                    self.jugador.Saltar()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and self.jugador.cambioX < 0:
                    self.jugador.Detener()
                if event.key == pygame.K_RIGHT and self.jugador.cambioX > 0:
                    self.jugador.Detener()

    def LogicaEjecucion(self):
        '''
        Este método se ejecuta por cada fotograma.
        Actualiza la posición de los objetos y la interacción
        entre los mismos.

        '''
        if not self.gameOver:
            self.listaSprites.update()
            self.starGame = True

            # Verificar si el jugador posee vidas
            if self.jugador.muerto:
                self.gameOver = True

            # Evitar que el jugador sobrepase los límites de la pantalla
            if self.jugador.rect.left < 0:
                 self.jugador.rect.left = 0

            if self.jugador.rect.right > ANCHO:
                 self.jugador.rect.right = ANCHO

            # Si el jugador se aproxima al borde derecho, desplazamos
            # el nivel hacia la izquierda
            if self.jugador.rect.x >= ANCHO / 2:
                desplazarX = self.jugador.rect.x - (ANCHO / 2)
                self.jugador.rect.x = ANCHO / 2
                self.niveles[self.nivelActual].Desplazar(-desplazarX)

            # Si el jugador se aproxima hacia el borde izquierdo,
            # desplazamos el nivel hacia la derecha
            if self.jugador.rect.x <= ANCHO / 4:
                desplazarX = (ANCHO / 4) - self.jugador.rect.x
                self.jugador.rect.x = ANCHO / 4
                self.niveles[self.nivelActual].Desplazar(desplazarX)

            # Si el jugador llega al final del nivel, pasar al nivel siguiente
            posicionActual = self.jugador.rect.x + \
                self.niveles[self.nivelActual].desplazamiento
            if posicionActual < self.niveles[self.nivelActual].limiteNivel:
                self.jugador.rect.x = ANCHO / 3
                if self.nivelActual < self.nivelMax:
                    # self.nivelActual += 1
                    # self.jugador.nivel = self.niveles[self.nivelActual]
                    self.nivelSiguiente = True
                else:
                    self.gameOver = True


    def Desplegar(self, pantalla):
        '''
        Dibuja los objetos sobre la superficie seleccionada.

        Parámetros:
        pantalla --> La superficie sobre la cual se dibujan los objetos.

        '''
        # pantalla.fill(BLANCO)

        if self.inicioJuego:
            if not self.gameOver:
                self.niveles[self.nivelActual].Dibujar(pantalla)
                self.listaSprites.draw(pantalla)

            if self.gameOver and self.jugador.muerto:
                PANTALLA.blit(self.imgPerder, (0, 0))
                pygame.display.flip()

            if self.nivelSiguiente:
                PANTALLA.blit(self.fondoNivelCompleto, (0, 0))
                pygame.display.flip()
                fpsClock.tick(0.50)
                self.nivelSiguiente = False
                self.nivelActual += 1
                self.jugador.nivel = self.niveles[self.nivelActual]

            if self.gameOver and not self.jugador.muerto:
                PANTALLA.blit(self.imgGanar, (0, 0))
                pygame.display.flip()
                fpsClock.tick(0.50)
                self.__init__()

        else:
            if self.nivelActual == 0:
                self.MenuPrincipal()
            else:
                self.inicioJuego = True
                self.reproducir = True

        pygame.display.flip()



    def MenuPrincipal(self):
        while not self.inicioJuego:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            self.Desplazar()
            PANTALLA.blit(self.imgMenuPrincipal, (0, 0))
            PANTALLA.blit(self.flecha,
                          (210, self.posicionOpcionY))
            pygame.display.flip()
            fpsClock.tick(10)
        PANTALLA.fill(BLANCO)
        pygame.display.flip()


    def Desplazar(self):
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_UP]:
            if self.posicionOpcionY > 400:
                self.posicionOpcionY -= 35
                self.opcion -= 1
        if tecla[pygame.K_DOWN]:
            if self.posicionOpcionY < 435:
                self.posicionOpcionY += 35
                self.opcion += 1
        if tecla[pygame.K_RETURN]:
            if self.opcion == 1:
                self.nivelActual = 0
                self.inicioJuego = True
            else:
                exit()


def main():
    '''
    Función principal del programa.

    '''
    # Título del juego
    pygame.display.set_caption('Adventure Girl')

    # Ocultar el cursor del mouse
    pygame.mouse.set_visible(False)

    # Controlador del ciclo principal
    hecho = False

    # Crear una instancia de clase Game
    juego = Game()

    while not hecho:
        # Procesar los eventos (pulsaciones del teclado, clic del ratón...)
        hecho = juego.ProcesarEventos()

        # Actualizar las posiciones de todos los objetos en pantalla
        juego.LogicaEjecucion()

        # Dibujar todos los objetos
        juego.Desplegar(PANTALLA)

        # Realizar una pausa hasta el siguiente fotograma
        fpsClock.tick(60)

    # Salir de la ventana de juego
    pygame.quit()


# Llamar a la función principal
if __name__ == '__main__':
    main()
