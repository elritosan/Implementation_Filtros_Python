from PIL import Image, ImageEnhance

def color_temperature(image, temperature):
    """
    Aplica un ajuste de temperatura de color a la imagen.
    
    Parámetros:
        - image: Imagen (PIL.Image) sobre la que se aplicará el filtro.
        - temperature: Valor numérico para ajustar la temperatura de color.
          Valores positivos = tonos cálidos (amarillos/rojos).
          Valores negativos = tonos fríos (azules).
          
    Retorna:
        - Imagen ajustada con el cambio de temperatura de color.
    """
    if not isinstance(temperature, (int, float)):
        raise ValueError("La temperatura debe ser un número.")

    # Convertir la imagen a modo RGB si no lo está
    if image.mode != "RGB":
        image = image.convert("RGB")

    # Separar canales R, G y B
    r, g, b = image.split()

    # Ajustar los canales para simular el efecto de temperatura de color
    if temperature > 0:  # Colores cálidos
        r = r.point(lambda i: min(255, i + temperature))
        b = b.point(lambda i: max(0, i - temperature))
    elif temperature < 0:  # Colores fríos
        r = r.point(lambda i: max(0, i + temperature))
        b = b.point(lambda i: min(255, i - temperature))
    
    # Combinar los canales ajustados
    adjusted_image = Image.merge("RGB", (r, g, b))
    
    return adjusted_image
