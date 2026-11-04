import numpy as np


class ObjetoIndustrial:
  """Representa una pieza u objeto industrial que circula por la planta.

  Almacena su identificador, tipo, forma geométrica, segmento actual y la
  información de su cuerpo/geom dentro de la simulación de MuJoCo.
  """

  def __init__(
      self,
      id_objeto: int,
      tipo: str,
      forma: str,
      segmento: int,
      body_id: int = None,
  ):
    self.id_objeto = id_objeto
    self.tipo = tipo
    self.forma = forma
    self.segmento = segmento
    self.body_id = body_id
    self.posicion = np.zeros(3)

  def actualizar_posicion(self, nueva_posicion):
    """Actualiza la posición tridimensional del objeto en la simulación."""
    self.posicion = np.array(nueva_posicion)

  def obtener_pose(self) -> np.ndarray:
    """Devuelve la posición actual del objeto."""
    return self.posicion