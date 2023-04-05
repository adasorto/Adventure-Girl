import pygame
from utility import Utility
from constantes import *
from plataforma import Plataforma


class Jugador(pygame.sprite.Sprite):
    '''
    Esta clase representa al protagonista del juego.

    Se encarga de todas las acciones del protagonista.

    '''

    def __init__(self, x, y):
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

        # Vidas del jugador
        self.vidas = 1
        self.muerto = False

        # Estas listas contienen las imágenes para la animación
        # al caminar del jugador.
        self.caminarIzq = list()
        self.caminarDer = list()

        # Dirección hacia la que vé el jugador
        self.direccion = None

        # Obtener todas las imágenes hacia la derecha
        image = self.utility.CargarImagen('Walk1.png')
        image = pygame.transform.scale(image, (110, 110))
        self.caminarDer.append(image)

        image = self.utility.CargarImagen('Walk2.png')
        image = pygame.transform.scale(image, (110, 110))
        self.caminarDer.append(image)

        image = self.utility.CargarImagen('Walk3.png')
        image = pygame.transform.scale(image, (110, 110))
        self.caminarDer.append(image)

        image = self.utility.CargarImagen('Walk4.png')
        image = pygame.transform.scale(image, (110, 110))
        self.caminarDer.append(image)

        image = self.utility.CargarImagen('Walk5.png')
        image = pygame.transform.scale(image, (110, 110))
        self.caminarDer.append(image)

        image = self.utility.CargarImagen('Walk6.png')
        image = pygame.transform.scale(image, (110, 110))
        self.caminarDer.append(image)

        image = self.utility.CargarImagen('Walk7.png')
        image = pygame.transform.scale(image, (110, 110))
        self.caminarDer.append(image)

        image = self.utility.CargarImagen('Walk8.png')
        image = pygame.transform.scale(image, (110, 110))
        self.caminarDer.append(image)

        # Obtener todas las imágenes hacia la izquierda
        # Como las imágenes ven hacia la derecha colocarlas
        # en espejo.
        image = self.utility.CargarImagen('Walk1.png')
        image = pygame.transform.scale(image, (110, 110))
        image = pygame.transform.flip(image, True, False)
        self.caminarIzq.append(image)

        image = self.utility.CargarImagen('Walk2.png')
        image = pygame.transform.scale(image, (110, 110))
        image = pygame.transform.flip(image, True, False)
        self.caminarIzq.append(image)

        image = self.utility.CargarImagen('Walk3.png')
        image = pygame.transform.scale(image, (110, 110)) 
        image = pygame.transform.flip(image, True, False)
        self.caminarIzq.append(image)

        image = self.utility.CargarImagen('Walk4.png')
        image = pygame.transform.scale(image, (110, 110))
        image = pygame.transform.flip(image, True, False)
        self.caminarIzq.append(image)

        image = self.utility.CargarImagen('Walk5.png')
        image = pygame.transform.scale(image, (110, 110))
        image = pygame.transform.flip(image, True, False)
        self.caminarIzq.append(image)

        image = self.utility.CargarImagen('Walk6.png')
        image = pygame.transform.scale(image, (110, 110))
        image = pygame.transform.flip(image, True, False)
        self.caminarIzq.append(image)

        image = self.utility.CargarImagen('Walk7.png')
        image = pygame.transform.scale(image, (110, 110))
        image = pygame.transform.flip(image, True, False)
        self.caminarIzq.append(image)

        image = self.utility.CargarImagen('Walk8.png')
        image = pygame.transform.scale(image, (110, 110))
        image = pygame.transform.flip(image, True, False)
        self.caminarIzq.append(image)

       
        # Imagen del salto del jugador
        self.salto = self.utility.CargarImagen('Jump.png')
        self.salto = pygame.transform.scale(self.salto, (110, 110))

        # Definir la imagen con la que inicia el jugador
        self.image = self.caminarDer[0]

        # Establecemos una referencia rectangular de la superficie
        self.rect = self.image.get_rect()

        # Establecemos los vectores de velocidad
        self.cambioX = 0
        self.cambioY = 0

        # Lista de todos los sprites en los cuales podemos colisionar
        self.nivel = None

    def update(self):
        '''
        Actualiza el jugador a la posición
        del cursor del mouse en la aplicación.

        '''
        # Verificar la gravedad
        self.CalcularGravedad()

        # Deplazamos el jugador a la izquierda/derecha
        posicion = self.rect.x + self.nivel.desplazamiento

        if self.direccion == 'D':
            frame = int((posicion // 30) % len(self.caminarDer))
            self.image = self.caminarDer[frame]
        elif self.direccion == 'I':
            frame = int((posicion // 30) % len(self.caminarIzq))
            self.image = self.caminarIzq[frame]

        self.rect.x += self.cambioX

        # Comprobar si hemos colisionado con algún objeto
        listaImpactos = pygame.sprite.spritecollide(self,
                                                    self.nivel.plataformas,
                                                    False)

        for impacto in listaImpactos:
            # Si nos estamos desplazando para la derecha,
            # hacemos que nuestro lado derecho sea el lado
            # izquierdo del objeto que hemos colisionado.
            if self.cambioX > 0:
                self.rect.right = impacto.rect.left
            elif self.cambioX < 0:
                # Caso contrario, si nos desplazamos hacia
                # la izquierda, hacemos lo opuesto.
                self.rect.left = impacto.rect.right

        # Desplazar hacia arriba/abajo
        self.rect.y += self.cambioY

        # Comprobramos si hemos colisionado con algún objeto
        listaImpactos = pygame.sprite.spritecollide(self,
                                                    self.nivel.plataformas,
                                                    False)

        for impacto in listaImpactos:
            # Reestablecemos nuestra posición basados
            # en la parte superior/inferior del objeto.
            if self.cambioY > 0:
                self.rect.bottom = impacto.rect.top
            elif self.cambioY < 0:
                self.rect.top = impacto.rect.bottom

            # Detenemos nuestro movimiento vertical
            self.cambioY = 0

        # Comprobamos si hemos colisionado con algún enemigo
        listaImpactos = pygame.sprite.spritecollide(self,
                                                    self.nivel.listaEnemigos,
                                                    False)

        for impacto in listaImpactos:
            self.vidas -= 1
            if self.vidas <= 0:
                self.muerto = True

    def CalcularGravedad(self):
        '''
        Realizamos un cálculo de la gravedad que
        afecta a nuestro protagonista.
        '''
        if self.cambioY == 0:
            self.cambioY = 1
            self.image = self.caminarDer[0]
        else:
            self.cambioY += .35
            self.image = self.salto

        # Verificar si nos encontramos sobre el fondo
        # de la superficie
        if self.rect.y >= ALTO - self.rect.height and self.cambioY >= 0:
            self.cambioY = 0
            self.rect.y = ALTO - self.rect.height

    def Saltar(self):
        '''
        Realiza los calculos que permiten al jugador realizar un salto
        en la superficie.

        '''
        # Descendemos verticalmente y observamos si existe
        # una plataforma debajo nuestro.
        self.rect.y += 2
        listaPlataforma = pygame.sprite.spritecollide(self,
                                                      self.nivel.plataformas,
                                                      False)
        self.rect.y -= 2

        # Si está listo para saltar, aumentamos nuestra
        # posición hacia arriba
        if len(listaPlataforma) > 0 or self.rect.bottom >= ALTO:
            self.cambioY = -10

    def Izquierda(self):
        '''
        Llamada cuando el usuario presione la tecla de movimiento
        del jugador hacia la izquierda.

        '''
        self.direccion = 'I'
        self.cambioX = -6

    def Derecha(self):
        '''
        Llamada cuando el usuario presione la tecla de movimiento
        del jugador hacia la derecha.

        '''
        self.direccion = 'D'
        self.cambioX = 6

    def Detener(self):
        '''
        Lllamada cuando el usuario no presiona ninguna tecla.

        '''
        if self.direccion == 'D':
            self.image = self.caminarDer[0]
        elif self.direccion == 'I':
            self.image = self.caminarIzq[0]

        self.direccion = None

        self.cambioX = 0