# 🛠️ Herramienta Automatizada de Nesting (Optimización de Chapa)

<p align="center">
  <img src="https://img.shields.io/badge/Status-En%20Desarrollo%20%F0%9F%9A%A7-orange?style=for-the-badge" alt="Status"/>
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
</p>

<p align="justify" style="font-family: 'Poppins', sans-serif; font-size: 1.1em;">
Este proyecto nace con el objetivo de automatizar y optimizar el proceso de corte de metales. Se trata de una herramienta de software capaz de interpretar geometrías complejas desde archivos CAD de formato estándar para calcular distribuciones eficientes (anidados) sobre planchas de chapa, minimizando drásticamente el desperdicio de material.
</p>

---

## 🎯 Estado Actual del Desarrollo

El software se encuentra actualmente en **fase de desarrollo activo**. Al día de hoy, el motor geométrico ya es capaz de:
* [x] Leer e interpretar entidades nativas de archivos **DXF** (`LINE`, `ARC`).
* [x] Procesar algoritmos de encadenamiento iterativo mediante lógica de continuidad geométrica.
* [x] Reconocer de forma independiente múltiples contornos cerrados (distinguiendo entre perímetros exteriores y calados/perforaciones internas).

---

## 🚀 Alcance del Proyecto Final

Una vez completado el ciclo de desarrollo, la herramienta ofrecerá una solución integral que permitirá:

1. **Clasificación Jerárquica Automática:** Identificación automática del contorno macro (perímetro de la pieza) mediante cálculo de *bounding boxes* (cuadros delimitadores) y asignación de sus calados internos (islas/agujeros).
2. **Algoritmo de Anidado (Nesting):** Computación geométrica para empaquetar de forma óptima múltiples piezas dentro de las dimensiones de una chapa estándar.
3. **Exportación Automatizada:** Generación de un nuevo archivo DXF con la distribución optimizada de corte lista para ser introducida en máquinas CNC (Láser/Plasma).

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
    <td><a href="https://ezdxf.mozman.at/">ezdxf</a> (Librería avanzada para procesamiento de estructuras DXF)</td>
  </tr>
  <tr>
    <td><b>Cálculo Matemático</b></td>
    <td><code>math</code> (Módulo nativo para trigonometría y vectores)</td>
  </tr>
</table>

---

## 🏗️ Próximos Pasos (Roadmap)
- [ ] Implementar la función de cálculo de áreas y límites (*Bounding Box*) mediante `min()` y `max()`.
- [ ] Diseñar el algoritmo de colisión (*Point-in-Polygon*) para emparentar agujeros con sus piezas.
- [ ] Desarrollar la lógica de rotación y traslación de piezas para el acomodo en la chapa.