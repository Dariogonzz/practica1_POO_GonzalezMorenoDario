class Horno:
  """Encapsula el comportamiento del horno al final de la línea industrial,

  incluyendo el registro de piezas recibidas, el control de la temperatura
  y la modificación visual de su color en la simulación MuJoCo.
  """

  def __init__(
      self,
      geom_id: int,
      temperatura_inicial: float = 20.0,
      temp_min: float = 0.0,
      temp_max: float = 200.0,
  ):
    self.numero_piezas = 0
    self.temperatura = temperatura_inicial
    self.geom_id = geom_id
    self.temp_min = temp_min
    self.temp_max = temp_max
    self.activo = True

  def registrar_pieza(self):
    """Incrementa el contador de piezas recibidas en el horno."""
    self.numero_piezas += 1

  def aumentar_temperatura(self, incremento: float):
    """Aumenta la temperatura actual del horno respetando el límite máximo."""
    self.temperatura = min(self.temp_max, self.temperatura + incremento)

  def disminuir_temperatura(self, decremento: float):
    """Disminuye la temperatura actual del horno respetando el límite mínimo."""
    self.temperatura = max(self.temp_min, self.temperatura - decremento)

  def obtener_temperatura(self) -> float:
    """Devuelve la temperatura actual del horno."""
    return self.temperatura

  def actualizar_color(self, model):
    """Refleja visualmente la temperatura actual del horno en MuJoCo

    modificando el color RGBA del elemento gráfico (geom) asociado.
    """
    if self.temperatura < 50.0:
      color = [0.1, 0.3, 1.0, 1.0]  # Azul (Temperatura baja / Frío)
    elif self.temperatura < 100.0:
      color = [1.0, 0.6, 0.1, 1.0]  # Naranja / Amarillo (Temperatura media)
    else:
      color = [1.0, 0.1, 0.1, 1.0]  # Rojo (Temperatura alta)

    # Actualización en el modelo de MuJoCo si el ID es válido
    if self.geom_id is not None:
      model.geom_rgba[self.geom_id] = color