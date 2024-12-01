import cv2
import numpy as np
import matplotlib.pyplot as plt

# Guardamos las imagenes en la carpeta 'imgs'
imgs_path = "./imgs"

# Función para mostrar y/o guardar imagenes
def manage_image_display(img, title="Image", display_img=True, save_img=False):
    """
    Muestra y/o guarda una imagen.

    :param img:         Imagen de entrada
    :param title:       Título de la imagen, usado también como nombre de archivo al guardar.
    :param display_img: Bool que indica si se debe mostrar la imagen.
    :param save_img:    Bool que indica si se debe guardar la imagen.
    """

    # Mostrar la imagen si display_img es True
    if display_img:
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.axis('off')
        plt.title(title)
        plt.show()
    
    # Guardar la imagen si save_img es True
    if save_img:
        filename = f"{imgs_path}/{title}.jpg"
        cv2.imwrite(filename, img)

# Función para cargar la imagen y redimensionarla
def ajustar_imagen(img, tamaño=(1024, 1024)):
    img_resized = cv2.resize(img, tamaño)
    return img_resized

# Función para dividir la imagen en 4 sub-imágenes
def dividir_imagen(img):
    imgs = []
    altura, ancho, _ = img.shape
    mitad_alto = altura // 2
    mitad_ancho = ancho // 2

    imgs.append(img[:mitad_alto, :mitad_ancho])
    imgs.append(img[:mitad_alto, mitad_ancho:])
    imgs.append(img[mitad_alto:, :mitad_ancho])
    imgs.append(img[mitad_alto:, mitad_ancho:])

    return imgs

# Función de ecualización
def ecualizar_imagen(imagen, display_hist=False, save_hist=False, title="CompDeHistogramas"):
    # Separamos la imagen en sus canales
    canales = cv2.split(imagen)

    # Ecualizamos cada canal
    canales_ec = [cv2.equalizeHist(canal) for canal in canales]

    # Juntamos los 3 canales nuevamente
    imagen_ecualizada = cv2.merge(canales_ec)

    if display_hist or save_hist:
        # Crear el gráfico con 6 subgráficos para los histogramas
        plt.figure(figsize=(12, 8))

        # Histogramas antes de la ecualización (Imagen original)
        # Subgráfico 1: Histograma del canal Azul (B)
        plt.subplot(2, 3, 1)
        plt.hist(canales[0].ravel(), bins=256, histtype='step', color='blue')
        plt.title('Histograma Original - Azul')
        plt.xlim(0, 256)

        # Subgráfico 2: Histograma del canal Verde (G)
        plt.subplot(2, 3, 2)
        plt.hist(canales[1].ravel(), bins=256, histtype='step', color='green')
        plt.title('Histograma Original - Verde')
        plt.xlim(0, 256)

        # Subgráfico 3: Histograma del canal Rojo (R)
        plt.subplot(2, 3, 3)
        plt.hist(canales[2].ravel(), bins=256, histtype='step', color='red')
        plt.title('Histograma Original - Rojo')
        plt.xlim(0, 256)

        # Histogramas después de la ecualización (Imagen ecualizada)
        # Subgráfico 4: Histograma del canal Azul (B) - Ecualizado
        plt.subplot(2, 3, 4)
        plt.hist(canales_ec[0].ravel(), bins=256, histtype='step', color='blue')
        plt.title('Histograma Ecualizado - Azul')
        plt.xlim(0, 256)

        # Subgráfico 5: Histograma del canal Verde (G) - Ecualizado
        plt.subplot(2, 3, 5)
        plt.hist(canales_ec[1].ravel(), bins=256, histtype='step', color='green')
        plt.title('Histograma Ecualizado - Verde')
        plt.xlim(0, 256)

        # Subgráfico 6: Histograma del canal Rojo (R) - Ecualizado
        plt.subplot(2, 3, 6)
        plt.hist(canales_ec[2].ravel(), bins=256, histtype='step', color='red')
        plt.title('Histograma Ecualizado - Rojo')
        plt.xlim(0, 256)

        if display_hist:
            # Mostrar histogramas
            plt.tight_layout()
            plt.show()

        if save_hist:
            # Guardar histogramas
            filename = f"{imgs_path}/{title}.jpg"
            plt.savefig(filename)
        
        plt.close()

    return imagen_ecualizada


# Función para contar los objetos binarios (células) en una imagen binaria
def contar_objetos(img_mask):
    # Encontrar contornos
    contornos, _ = cv2.findContours(img_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Calcular el área promedio de los objetos
    areas = [cv2.contourArea(contorno) for contorno in contornos]
    area_promedio = np.mean(areas) if areas else 0

    # Cantidad de objetos
    num_objetos = len(contornos)

    return num_objetos, area_promedio


# Aplicar una operación morfológica de apertura
def OpMorfApertura(img_binaria, kernel_size = 7):

    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    img_apertura = cv2.morphologyEx(img_binaria, cv2.MORPH_OPEN, kernel)

    return img_apertura



# Función para graficar la evolución de objetos y áreas
def graficar_evolucion_objetos_areas(kernel_sizes, objetos, areas,  
    display_hist=False, save_hist=False, title="NumObjetosVsKernelSize"):
    """
    Grafica la evolución del número de objetos y el área promedio en función del tamaño del kernel.
    """
    plt.figure(figsize=(12, 6))

    # Evolución del número de objetos
    plt.subplot(1, 2, 1)
    plt.plot(kernel_sizes, objetos, marker='o', linestyle='-', color='b')
    plt.title("Evolución del número de objetos")
    plt.xlabel("Tamaño del kernel")
    plt.ylabel("Cantidad de objetos")
    plt.grid(True)

    # Evolución del área promedio
    plt.subplot(1, 2, 2)
    plt.plot(kernel_sizes, areas, marker='o', linestyle='-', color='r')
    plt.title("Evolución del área promedio")
    plt.xlabel("Tamaño del kernel")
    plt.ylabel("Área promedio")
    plt.grid(True)

    plt.tight_layout()

    if display_hist:
        # Mostrar histogramas
        plt.tight_layout()
        plt.show()

    if save_hist:
        # Guardar histogramas
        filename = f"{imgs_path}/{title}.jpg"
        plt.savefig(filename)
    
    plt.close()


# Fusiona la imagen original con la máscara binaria aplicando un color específico.
def fusionar_imagenes(imagen, img_mask, color=(255, 0, 0), transparencia=0.5):

    # Crear una copia para no modificar la imagen original
    imagen_fusionada = imagen.copy()

    # Crear una máscara de 3 canales con el color deseado
    mask_colored = np.zeros_like(imagen_fusionada)
    mask_colored[img_mask > 0] = color  # Aplica el color solo en las zonas de la máscara

    # Combinar la imagen original con la máscara coloreada (con transparencia configurable)
    imagen_fusionada = cv2.addWeighted(imagen_fusionada, 1, mask_colored, transparencia, 0)

    return imagen_fusionada

