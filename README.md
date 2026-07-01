# 🛠️ Herramienta Automatizada de Nesting (Optimización de Chapa)

<p align="center">
  <img src="https://img.shields.io/badge/Status-En%20Desarrollo%20%F0%9F%9A%A7-orange?style=for-the-badge" alt="Status"/>
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
</p>

<p align="justify" style="font-family: 'Poppins', sans-serif; font-size: 1.1em;">
Este proyecto busca automatizar parte del proceso de corte de chapa a partir de geometrías contenidas en archivos DXF. Actualmente, la lógica implementada permite leer un dibujo, extraer entidades geométricas, reconstruir contornos, separar el contorno principal de los posibles calados internos y, además, procesar lotes de piezas para generar un primer acomodo en la chapa mediante un algoritmo inicial de nesting.
</p>

---

## 🎯 Estado actual del desarrollo

El proyecto se encuentra en una fase de desarrollo funcional intermedia. Hasta el momento, las siguientes capacidades están implementadas y verificables en el código:

- [x] Lectura de archivos DXF con la librería ezdxf.
- [x] Procesamiento de entidades de tipo LINE y ARC.
- [x] Conversión de entidades en segmentos geométricos simples.
- [x] Reconstrucción de contornos cerrados a partir de segmentos conectados.
- [x] Identificación de un contorno principal o macrocontorno.
- [x] Cálculo de límites por coordenadas con min() y max().
- [x] Detección de calados internos que quedan dentro del contorno principal.
- [x] Generación de un resultado estructurado en forma de diccionario con el archivo procesado, límites, contorno macro y calados válidos.
- [x] Procesamiento por lote de múltiples archivos DXF desde una carpeta.
- [x] Cálculo del área de cada pieza para ordenar el procesamiento por tamaño.
- [x] Implementación de un motor de nesting inicial basado en posicionamiento bottom-left con comprobación de colisiones.

---

## 🔧 Funcionalidades ya incorporadas

El flujo actual del programa realiza lo siguiente:

1. Lee uno o varios archivos DXF desde una carpeta de entrada.
2. Recorre las entidades del dibujo.
3. Convierte las líneas y arcos en pares de puntos.
4. Une los segmentos para formar contornos cerrados.
5. Selecciona el contorno de mayor tamaño como contorno macro.
6. Compara los demás contornos con los límites del macrocontorno para identificar calados internos.
7. Ordena las piezas por área y aplica un primer algoritmo de nesting para ubicarlas en una chapa.
8. Devuelve un resultado listo para una siguiente etapa de análisis, optimización o exportación.

---

## 🚧 Funcionalidades pendientes

Las siguientes partes aún no están implementadas en el código actual:

- [x] Algoritmo inicial de nesting para ubicar piezas dentro de una chapa.
- [ ] Rotación y traslación automática de piezas.
- [ ] Exportación o generación de un nuevo archivo DXF con la distribución resultante.
- [ ] Interfaz de usuario o flujo de entrada más flexible.

---

## 🧰 Tecnologías y Librerías

El ecosistema del proyecto está construido sobre tecnologías eficientes y especializadas en el manejo de vectores geométricos:

<table>
  <tr>
    <td><b>Lenguaje Base</b></td>
    <td>Python 3.x</td>
  </tr>
  <tr>
    <td><b>Manipulación CAD</b></td>
    <td><a href="https://ezdxf.mozman.at/" target="_blank">ezdxf</a> (Librería avanzada para procesamiento de estructuras DXF)</td>
  </tr>
  <tr>
    <td><b>Cálculo Matemático</b></td>
    <td><code>math</code> (Módulo nativo para trigonometría y vectores)</td>
  </tr>
</table>

---

## 🏗️ Próximos Pasos (Roadmap)
- [x] Implementar la función de cálculo de áreas y límites (*Bounding Box*) mediante `min()` y `max()`.
- [x] Diseñar el algoritmo de colisión (*Point-in-Polygon*) para emparentar calados con sus piezas.
- [x] Implementar un primer motor de acomodo bottom-left con validación de colisiones y puntos candidatos.
- [ ] Desarrollar la lógica de rotación y traslación de piezas para el acomodo en la chapa.