import cv2
import argparse

from utils import *

parser = argparse.ArgumentParser(description='Procesamiento de imágenes con OpenCV')
parser.add_argument('--guardar_imagenes', '-save', action='store_true',
                    help='Permite guardar las imagenes generadas')
parser.add_argument('--no_mostrar_imagenes', '-dont_display', action='store_true',
                    help='Permite no mostrar las imagenes generadas')
args = parser.parse_args()

def main():

    disp_flag = not(args.no_mostrar_imagenes)  # Mostramos las imagenes generadas
    save_flag = args.guardar_imagenes  # Guardamos las imagenes generadas

    # Cargar y ajustar la imagen
    imagen = cv2.imread('./data/Test1.jpg')
    imagen = ajustar_imagen(imagen)
    manage_image_display(imagen, "ResizedImg", disp_flag, save_flag)

    # Dividir la imagen en 4 sub-imágenes y mostrarlas  
    labels = ["Cuad 1", "Cuad 2", "Cuad 3", "Cuad 4"]
    imgs = dividir_imagen(imagen)
    for img, label in zip(imgs, labels):
        manage_image_display(img, label, disp_flag, save_flag)

    # Aplicar ecualización a la imagen y mostrarla
    imagen_ecualizada = ecualizar_imagen(imagen, display_hist=disp_flag, save_hist=save_flag)
    manage_image_display(imagen_ecualizada, "ImgEcualizada", disp_flag, save_flag)

    # Cargar la máscara binaria 
    img_mask = cv2.imread('./data/MASK.tif', cv2.IMREAD_GRAYSCALE)

    # Reajustamos la máscara al tamaño de 1024x1024
    img_mask = ajustar_imagen(img_mask)
    
    # Para mostrar la imagen, esta debe tener valores entre 0 y 255
    img_mask_scaled = img_mask*255 # Conversión binaria a 8 bits
    # Mostramos y guardamos la visualización de la máscara
    manage_image_display(img_mask_scaled, "ImgMask", disp_flag, save_flag)

    # Contamos la cantidad de objetos previa a la operación de apertura
    num_objetos, area_promedio = contar_objetos(img_mask)
    print(f"==> Resultados pre-apertura")
    print(f"> Cantidad de objetos binarios (células): {num_objetos}")
    print(f"> Promedio del área de los objetos: {area_promedio}")

    # Aplicamos la operación de apertura
    img_mask_apertura = OpMorfApertura(img_mask, kernel_size=8)
    # Guardamos la visualización del resultado
    img_mask_scaled = img_mask_apertura * 255 
    manage_image_display(img_mask_scaled, "ImgMaskApertura", disp_flag, save_flag)

    # Contamos la cantidad de objetos previa a la operación de apertura
    num_objetos, area_promedio = contar_objetos(img_mask_apertura)

    print(f"==> Resultados post-apertura")
    print(f"> Cantidad de objetos binarios (células): {num_objetos}")
    print(f"> Promedio del área de los objetos: {area_promedio}")

    # Podemos variar el tamaño del kernel de apertura 
    # y contar los objetos para cada caso
    objetos = []
    areas = []
    kernel_sizes = range(1, 21)
    for kernel_size in kernel_sizes:
        img_mask_apertura = OpMorfApertura(img_mask, kernel_size=kernel_size)
        num_objetos, area_promedio = contar_objetos(img_mask_apertura)
        objetos.append(num_objetos)        
        areas.append(area_promedio) 

    graficar_evolucion_objetos_areas(kernel_sizes, 
            objetos, areas, disp_flag, save_flag)

    # Conclusiones:
    # - A mayor tamaño de kernel se separan mas objetos
    # - Si el tamaño del kernel es demasiado grande 
    #   los objetos de menor tamaño desaparecen

    # # Fusionar la imagen original con la máscara
    imagen_fusionada = fusionar_imagenes(imagen, img_mask, color=(255, 0, 0))  # Azul
    manage_image_display(imagen_fusionada, "ImgConMascaraAplicada", disp_flag, save_flag)



if __name__ == '__main__':
    main()