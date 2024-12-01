# Desafío Técnico Imágenes - DigPatho

Este repositorio contiene el código creado para la realización un desafío técnico sobre procesamiento y análisis de imágenes médicas.

## Funcionamiento

### Ejecución por Defecto

Al ejecutar el código sin parámetros adicionales, se mostrarán todas las imágenes generadas durante el procesamiento:

```bash
python3 main.py
```

Este comando ejecuta el procesamiento completo de las imágenes y las muestra de manera interactiva.

### Guardar Imágenes Sin Mostrar

Para generar y guardar las imágenes sin mostrarlas en pantalla, se utiliza la siguiente opción. Las imágenes generadas se guardarán dentro de la carpeta `imgs`:

```bash
python3 main.py -dont_display -save
```

- **`-dont_display`**: No mostrará las imágenes durante la ejecución.
- **`-save`**: Guardará las imágenes generadas en la carpeta `imgs`.

---

### Funciones Principales

A continuación se describen las principales funciones implementadas en el código:

1. **`manage_image_display(img, title="Image", display_img=True, save_img=False)`**  
   Muestra y/o guarda una imagen. Esta función permite visualizar la imagen en una ventana de matplotlib si `display_img` es `True` y, opcionalmente, guarda la imagen en el directorio `imgs` si `save_img` está habilitado.  
   - **Parámetros**:
     - `img`: Imagen de entrada.
     - `title`: Título que se utiliza tanto para mostrar como para guardar la imagen.
     - `display_img`: Determina si se debe mostrar la imagen.
     - `save_img`: Determina si se debe guardar la imagen.

2. **`ajustar_imagen(img, tamaño=(1024, 1024))`**  
   Redimensiona la imagen a un tamaño especificado. Por defecto, ajusta la imagen a 1024x1024 píxeles.  
   - **Parámetros**:
     - `img`: Imagen a redimensionar.
     - `tamaño`: Tupla que define el tamaño de la imagen de salida (por defecto `(1024, 1024)`).

3. **`dividir_imagen(img)`**  
   Divide una imagen en 4 sub-imágenes, dividiendo tanto a lo largo de la altura como del ancho.  
   - **Parámetros**:
     - `img`: Imagen a dividir.
   - **Salida**: Lista con las 4 sub-imágenes.

4. **`ecualizar_imagen(imagen, display_hist=False, save_hist=False, title="CompDeHistogramas")`**  
   Realiza la ecualización de histograma sobre cada canal de la imagen (rojo, verde y azul). Además, permite visualizar y guardar los histogramas de las imágenes antes y después de la ecualización.  
   - **Parámetros**:
     - `imagen`: Imagen de entrada para ecualizar.
     - `display_hist`: Determina si se deben mostrar los histogramas generados.
     - `save_hist`: Determina si se deben guardar los histogramas.
     - `title`: Título para el archivo guardado.
   - **Salida**: Imagen ecualizada.

5. **`contar_objetos(img_mask)`**  
   Encuentra y cuenta los objetos binarios (como células) en una imagen binaria utilizando contornos. También calcula el área promedio de los objetos encontrados.  
   - **Parámetros**:
     - `img_mask`: Imagen binaria donde los objetos son visibles.
   - **Salida**: Número de objetos y área promedio de los objetos.

6. **`OpMorfApertura(img_binaria, kernel_size=7)`**  
   Aplica una operación morfológica de apertura a una imagen binaria. La operación de apertura es útil para eliminar pequeñas áreas de ruido en las imágenes binarizadas.  
   - **Parámetros**:
     - `img_binaria`: Imagen binaria sobre la cual aplicar la operación.
     - `kernel_size`: Tamaño del núcleo utilizado en la operación morfológica (por defecto 7x7).

7. **`graficar_evolucion_objetos_areas(kernel_sizes, objetos, areas, display_hist=False, save_hist=False, title="NumObjetosVsKernelSize")`**  
   Grafica la evolución del número de objetos y el área promedio en función del tamaño del kernel utilizado en la operación morfológica.  
   - **Parámetros**:
     - `kernel_sizes`: Lista de tamaños de kernel utilizados.
     - `objetos`: Lista del número de objetos para cada tamaño de kernel.
     - `areas`: Lista del área promedio para cada tamaño de kernel.
     - `display_hist`: Determina si se deben mostrar los gráficos.
     - `save_hist`: Determina si se deben guardar los gráficos generados.
     - `title`: Título para el archivo guardado.

8. **`fusionar_imagenes(imagen, img_mask, color=(255, 0, 0), transparencia=0.5)`**  
   Fusiona la imagen original con una máscara binaria, aplicando un color específico en las áreas indicadas por la máscara. Se puede controlar la transparencia de la máscara aplicada.  
   - **Parámetros**:
     - `imagen`: Imagen de entrada.
     - `img_mask`: Máscara binaria que indica las áreas de interés.
     - `color`: Color aplicado a la máscara (por defecto rojo: `(255, 0, 0)`).
     - `transparencia`: Grado de transparencia de la máscara sobre la imagen (por defecto 0.5).

---

### Conclusión

Este proyecto muestra el uso típico de la librería OpenCV de Python para procesar, analizar y visualizar imágenes. A través de diversas funciones, se abordan tareas comunes de preprocesamiento, manipulación y análisis de imágenes, como redimensionado, ecualización, manipulación de máscaras y operaciones morfológicas.

---
