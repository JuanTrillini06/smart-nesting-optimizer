# Documentación del proyecto

## 1. Descripción general

Este proyecto procesa archivos DXF de geometrías de chapa y convierte la información de las entidades geométricas en una estructura de contornos que puede servir como base para una etapa posterior de nesting.

El flujo actual del programa consiste en:

1. Leer un archivo DXF.
2. Extraer entidades geométricas de tipo LINE y ARC.
3. Convertir esas entidades en segmentos geométricos.
4. Reconstruir contornos cerrados a partir de segmentos conectados.
5. Identificar el contorno principal o macrocontorno.
6. Detectar los calados o agujeros internos mediante comparación de límites.
7. Guardar el resultado en un diccionario con los datos procesados.

---

## 2. Estado verificado del proyecto

La documentación que sigue refleja únicamente lo que está implementado en los archivos actuales del proyecto.

### Capacidades implementadas

- Lectura de archivos DXF con ezdxf.
- Manejo de entidades LINE y ARC.
- Extracción de coordenadas de inicio y fin de líneas y arcos.
- Reconstrucción de contornos cerrados.
- Identificación de un contorno principal mediante comparación de áreas aproximadas.
- Cálculo de límites del contorno con min() y max().
- Detección de calados internos que quedan dentro del contorno macro.
- Generación de una estructura de salida con los resultados del procesamiento.

### Limitaciones actuales

- No se ha implementado todavía un algoritmo de nesting completo.
- No existe una lógica de rotación o traslación automática para piezas.
- No hay exportación de resultados a un nuevo archivo DXF.
- No se ha incorporado una interfaz de usuario o un flujo de entrada más flexible.

---

## 3. Estructura del proyecto

```text
anidados/
├── encontrar_entidades.py
├── README.md
├── DOCUMENTACION_PROYECTO.md
├── files/
│   ├── 00.C.TR.00342.dxf
│   └── 00.C.VI.00711.dxf
└── funciones/
    ├── fun_encontrar_contornos.py
    ├── fun_extraer_atributos.py
    ├── funciones_de_contorno.py
    └── __pycache__/
```

---

## 4. Descripción de carpetas y archivos

### 4.1 Carpeta raíz

Contiene los archivos principales del proyecto.

- Archivo: encontrar_entidades.py
  - Es el script principal.
  - Lee un archivo DXF, recorre sus entidades, obtiene segmentos, reconstruye contornos, identifica el contorno macro y detecta calados internos.

- Archivo: README.md
  - Documentación general del proyecto.
  - Resume el estado actual, las funcionalidades implementadas y las pendientes.

- Archivo: DOCUMENTACION_PROYECTO.md
  - Documento técnico del proyecto.
  - Describe la arquitectura, módulos, funciones y variables del código actual.

### 4.2 Carpeta files

Almacena los archivos DXF usados como ejemplo o entrada.

- 00.C.TR.00342.dxf
  - Archivo de prueba utilizado por el script principal.

- 00.C.VI.00711.dxf
  - Archivo adicional disponible en el proyecto.

### 4.3 Carpeta funciones

Contiene los módulos con la lógica específica del procesamiento geométrico.

---

## 5. Archivo principal: encontrar_entidades.py

### 5.1 Propósito

Este archivo es el punto de entrada del programa. Su tarea es ejecutar el flujo completo de procesamiento del dibujo y preparar los resultados para una siguiente etapa.

### 5.2 Funciones y elementos usados

No define funciones propias. Utiliza funciones importadas desde la carpeta funciones.

### 5.3 Variables principales

- doc
  - Almacena el contenido del archivo DXF leído con ezdxf.
  - Se usa para acceder al model space del dibujo.

- msp
  - Representa el espacio modelo del dibujo.
  - Se recorre para obtener las entidades.

- segmentos
  - Lista que acumula los segmentos geométricos extraídos.
  - Se usa como entrada para la detección de contornos.

- entidad
  - Variable temporal que guarda el tipo de entidad detectada.
  - Permite decidir si se debe procesar como línea o arco.

- contornos
  - Lista con los contornos encontrados a partir de los segmentos.
  - Se usa para identificar el contorno macro y los calados.

- idx_macro
  - Índice del contorno que se considera el principal.

- perimetro_macro
  - Contorno seleccionado como pieza principal.

- limites_macro
  - Límites del contorno macro: x_min, x_max, y_min, y_max.

- posibles_calados
  - Lista de contornos restantes después de separar el macrocontorno.

- calados_validos
  - Lista de contornos internos considerados válidos como calados.

- pieza_procesada
  - Diccionario final con el resultado del procesamiento.

### 5.4 Uso de funciones importadas

- linea(entity)
  - Se usa cuando la entidad detectada es LINE.

- arco(entity)
  - Se usa cuando la entidad detectada es ARC.

- enocontrar_contornos(segmentos)
  - Se usa para reconstruir los contornos cerrados a partir de los segmentos.

- contorno_macro(contornos)
  - Se usa para encontrar el contorno principal.

- obtener_limites_contorno(perimetro_macro)
  - Se usa para calcular los límites del macrocontorno.

- calados_huerfanos(posibles_calados, limites_macro)
  - Se usa para filtrar los contornos internos.

### 5.5 Manejo de errores

El script incluye manejo de excepciones para:

- archivo no encontrado o no abierto,
- estructura DXF inválida o dañada.

---

## 6. Módulo: funciones/fun_extraer_atributos.py

### 6.1 Propósito

Este módulo convierte entidades DXF en estructuras geométricas simples, representadas como pares de puntos.

### 6.2 Funciones

#### 6.2.1 linea(entidad)

- Entrada: una entidad DXF de tipo LINE.
- Proceso: toma el punto inicial y final de la línea.
- Salida: una tupla con dos puntos: (inicio, fin).

Variables internas:

- inicio
  - Coordenadas del punto inicial.

- fin
  - Coordenadas del punto final.

Uso:

- Se invoca desde encontrar_entidades.py para entidades LINE.

#### 6.2.2 arco(entidad)

- Entrada: una entidad DXF de tipo ARC.
- Proceso: calcula el punto de inicio y fin del arco a partir del centro, radio y ángulos.
- Salida: una tupla con dos puntos: (inicio, fin).

Variables internas:

- centro
  - Coordenadas del centro del arco.

- radio
  - Valor del radio.

- angulos
  - Ángulos convertidos a radianes.

- inicio
  - Coordenadas del punto inicial del arco.

- fin
  - Coordenadas del punto final del arco.

Uso:

- Se invoca desde encontrar_entidades.py para entidades ARC.

---

## 7. Módulo: funciones/fun_encontrar_contornos.py

### 7.1 Propósito

Este módulo conecta segmentos entre sí para reconstruir contornos cerrados.

### 7.2 Funciones

#### 7.2.1 redondear_punto(punto)

- Entrada: una tupla con coordenadas.
- Proceso: redondea los valores de X e Y a dos decimales.
- Salida: un punto redondeado.

Uso:

- Se usa dentro de enocontrar_contornos para normalizar puntos y facilitar comparaciones.

#### 7.2.2 enocontrar_contornos(segmentos)

- Entrada: lista de segmentos representados como pares de puntos.
- Proceso:
  - toma el primer segmento,
  - construye un contorno inicial,
  - busca segmentos conectados por coincidencia de extremos,
  - agrega puntos hasta que ya no hay más conexiones.
- Salida: lista de contornos encontrados.

Variables internas:

- contornos_encontrados
  - Lista donde se acumulan los contornos construidos.

- primer_segmento
  - Segmento inicial para empezar un contorno.

- contorno_actual
  - Lista temporal con los puntos del contorno.

- punto_busqueda
  - Último punto del contorno usado para seguir la conexión.

- conexion
  - Variable de control que indica si se encontró un segmento conectado.

- segmento
  - Variable de iteración para recorrer los segmentos restantes.

Uso:

- Se invoca desde encontrar_entidades.py después de extraer los segmentos.

---

## 8. Módulo: funciones/funciones_de_contorno.py

### 8.1 Propósito

Este módulo analiza los contornos detectados para obtener límites y separar el perímetro principal de los posibles calados internos.

### 8.2 Funciones

#### 8.2.1 obtener_limites_contorno(contorno)

- Entrada: una lista de puntos que representa un contorno.
- Proceso: extrae los valores de x e y y devuelve sus límites.
- Salida: tupla con (x_min, x_max, y_min, y_max).

Variables internas:

- lista_x
  - Coordenadas X del contorno.

- lista_y
  - Coordenadas Y del contorno.

Uso:

- Se usa para obtener los límites de un contorno.
- Es invocada por contorno_macro y calados_huerfanos.

#### 8.2.2 contorno_macro(contornos)

- Entrada: lista de contornos.
- Proceso:
  - recorre todos los contornos,
  - calcula un área aproximada a partir de sus límites,
  - elige el de mayor área como contorno principal.
- Salida: índice del contorno macro dentro de la lista.

Variables internas:

- area_maxima
  - Valor mayor encontrado entre los contornos evaluados.

- indice
  - Índice del contorno actual en la iteración.

- contorno
  - Contorno evaluado.

- x_min, x_max, y_min, y_max
  - Límites del contorno actual.

- area
  - Área aproximada del rectángulo delimitador.

- indice_macro
  - Índice del contorno seleccionado como macrocontorno.

Uso:

- Se usa desde encontrar_entidades.py para seleccionar el contorno principal.

#### 8.2.3 calados_huerfanos(contornos, limites_macro)

- Entrada:
  - una lista de contornos candidatos,
  - los límites del contorno macro.
- Proceso:
  - compara los límites de cada contorno con los del macrocontorno,
  - conserva solo los que están completamente dentro del perímetro principal.
- Salida: lista de calados válidos.

Variables internas:

- x_min_p, x_max_p, y_min_p, y_max_p
  - Límites del contorno macro.

- calados_validos
  - Lista con los contornos internos válidos.

- x_min_h, x_max_h, y_min_h, y_max_h
  - Límites del contorno evaluado.

Uso:

- Se usa desde encontrar_entidades.py para separar los agujeros internos de la pieza principal.

---

## 9. Resumen del flujo de ejecución

El script principal sigue este orden:

1. Lee el archivo DXF.
2. Recorre sus entidades.
3. Convierte líneas y arcos en segmentos.
4. Reconstruye contornos cerrados.
5. Identifica el contorno principal.
6. Extrae sus límites.
7. Detecta los calados internos.
8. Guarda todo en un diccionario con los resultados del procesamiento.

---

## 10. Observaciones técnicas

- El proyecto usa la librería ezdxf para trabajar con archivos DXF.
- La lógica geométrica está basada en coordenadas y en la conexión de extremos de segmentos.
- El código actual está enfocado en la identificación de contornos y en la clasificación básica de la pieza.
- El nombre de la función enocontrar_contornos está escrito de forma no estándar, pero es la función que se usa actualmente en el flujo principal.
