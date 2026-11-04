import cv2
import numpy as np


class CamaraInspeccion:
  """Representa una cámara de inspección de la planta industrial.

  Se encarga de capturar frames desde MuJoCo, procesarlos mediante OpenCV
  para detectar la forma geométrica de los objetos y actualizar la variable
  booleana de control para detener la cinta correspondiente.
  """

  def __init__(self, id_camara: int, nombre_mjcf: str, cinta):
    self.id_camara = id_camara
    self.nombre_mjcf = nombre_mjcf
    self.cinta = cinta
    self.objeto_detectado = False
    self.forma_detectada = None
    self.imagen = None

  def capturar(self, renderer, data):
    """Actualiza la escena de MuJoCo con la cámara asociada y obtiene

    la imagen en formato BGR compatible con OpenCV.
    """
    renderer.update_scene(data, camera=self.nombre_mjcf)
    imagen_rgb = renderer.render()
    # Conversión de RGB (MuJoCo) a BGR (OpenCV)
    self.imagen = cv2.cvtColor(imagen_rgb, cv2.COLOR_RGB2BGR)
    return self.imagen

  def detectar_forma(self, imagen, area_minima: int = 300) -> str | None:
    """Procesa la imagen mediante filtrado HSV, morfología y contornos

    para identificar si hay un cuadrado, rectángulo o círculo.
    """
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

    # Máscara de color para aislar los objetos sobre la cinta oscura
    mask = cv2.inRange(
        hsv, np.array([0, 60, 40]), np.array([179, 255, 255])
    )

    # Limpieza de ruido con operaciones morfológicas
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Búsqueda de contornos externos
    contornos, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    forma = None
    for contorno in contornos:
      area = cv2.contourArea(contorno)
      if area < area_minima:
        continue

      perimetro = cv2.arcLength(contorno, True)
      if perimetro <= 0:
        continue

      # Aproximación poligonal para contar vértices
      aproximacion = cv2.approxPolyDP(contorno, 0.03 * perimetro, True)
      vertices = len(aproximacion)
      x, y, w, h = cv2.boundingRect(aproximacion)
      relacion_aspecto = w / float(h)
      
      circularidad = (4.0 * np.pi * area) / (perimetro * perimetro)

      # Clasificación geométrica según vértices y circularidad
      if vertices == 4:
        if 0.85 <= relacion_aspecto <= 1.15:
          forma = "cuadrado"
        else:
          forma = "rectangulo"
      elif vertices >= 6 and circularidad > 0.72:
        forma = "circulo"
      else:
        if circularidad > 0.78:
          forma = "circulo"
        else:
          forma = "desconocido"
      break  # Analizamos la primera pieza relevante encontrada

    return forma

  def actualizar(self, renderer, data):
    """Método principal de actualización: captura, procesa, actualiza

    la variable booleana de detección y detiene la cinta si procede.
    """
    imagen = self.capturar(renderer, data)
    self.forma_detectada = self.detectar_forma(imagen)
    
    # Actualización obligatoria de la variable booleana exigida por la práctica
    self.objeto_detectado = self.forma_detectada is not None

    # Comportamiento requerido: Si detecta una pieza, detiene la cinta asociada
    if self.objeto_detectado:
      self.cinta.detener()

    return imagen