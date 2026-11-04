import numpy as np


class CintaTransportadora:
  """Representa una cinta transportadora individual de la planta industrial,

  gestionando su propio estado y configuración de forma independiente (POO).
  """

  def __init__(
      self,
      id_cinta: int,
      velocidad: float,
      direccion: np.ndarray,
      activa: bool = True,
  ):
    self.id = id_cinta
    self.velocidad = velocidad
    self.direccion = np.array(direccion)
    self.activa = activa

  def arrancar(self):
    """Pone en marcha la cinta transportadora."""
    self.activa = True

  def detener(self):
    """Detiene la cinta transportadora (por ejemplo, al detectar una pieza)."""
    self.activa = False

  def conmutar(self):
    """Alterna el estado de marcha y parada de la cinta."""
    self.activa = not self.activa

  def esta_activa(self) -> bool:
    """Devuelve el estado actual de funcionamiento de la cinta."""
    return self.activa

  def actualizar(self):
    """Método de actualización periódica del movimiento de la cinta."""
    if self.activa:
      # Lógica de aplicación del movimiento físico sobre los objetos
      pass