import time
import numpy as np
from src.cinta_transportadora import CintaTransportadora
from src.camara_inspeccion import CamaraInspeccion
from src.horno import Horno
from src.robot import RobotPanda


class PlantaIndustrial:
    """Clase coordinadora principal de la planta industrial.

    Gestiona las instancias de cintas transportadoras, cámaras de inspección,
    horno, robot, objetos industriales y el bucle de la simulación MuJoCo.
    """

    def __init__(self):
        self.cintas = []
        self.camaras = []
        self.objetos = []
        self.horno = None
        self.robot = RobotPanda()
        
        # Variables de simulación (MuJoCo)
        self.model = None
        self.data = None
        self.renderer = None
        self.activa = True

    def inicializar(self):
        """Inicializa los modelos de MuJoCo, los IDs de elementos y crea

        las instancias reales de las clases de la planta.
        """
        print("Inicializando componentes de la Planta Industrial...")
        
        # Ejemplo de inicialización de cintas
        cinta_1 = CintaTransportadora(id_cinta=1, velocidad=0.05, direccion=np.array([1, 0, 0]))
        cinta_2 = CintaTransportadora(id_cinta=2, velocidad=0.05, direccion=np.array([0, 1, 0]))
        self.cintas = [cinta_1, cinta_2]

        # Inicialización del horno (asignando un ID de geometría de ejemplo)
        self.horno = Horno(geom_id=0, temperatura_inicial=20.0)

        # Inicialización de cámaras asociadas a sus respectivas cintas
        camara_1 = CamaraInspeccion(id_camara=1, nombre_mjcf="camara_1", cinta=cinta_1)
        self.camaras = [camara_1]

        print("Planta industrial inicializada correctamente con POO.")

    def actualizar(self):
        """Actualiza el estado físico de la simulación, procesa las cámaras,

        controla las cintas y actualiza los indicadores térmicos del horno.
        """
        # 1. Actualizar estado de las cintas y objetos
        for cinta in self.cintas:
            cinta.actualizar()

        # 2. Actualizar cámaras y comprobar detección visual
        # (Se asume que el renderer y data de MuJoCo están disponibles en ejecución real)
        if self.renderer and self.data:
            for camara in self.camaras:
                camara.actualizar(self.renderer, self.data)

        # 3. Gestionar temperatura y color visual del horno en MuJoCo
        if self.horno and self.model:
            # Ejemplo dinámico de incremento térmico regulado
            self.horno.aumentar_temperatura(0.01)
            self.horno.actualizar_color(self.model)

        # 4. Actualizar estado del robot y su cinemática inversa
        self.robot.actualizar()

    def procesar_teclado(self):
        """Gestiona los eventos de teclado para el control interactivo de la planta."""
        pass

    def ejecutar(self):
        """Bucle principal de ejecución (run loop) de la simulación."""
        self.inicializar()
        print("Ejecutando bucle principal de la planta industrial...")
        
        try:
            # Bucle orientativo de simulación
            while self.activa:
                self.actualizar()
                self.procesar_teclado()
                # Pequeña pausa para sincronizar tasa de refresco
                time.sleep(0.01)
        except KeyboardInterrupt:
            print("\nSimulación detenida por el usuario.")