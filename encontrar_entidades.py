import ezdxf
from funciones.fun_extraer_atributos import linea, arco
from funciones.fun_encontrar_contornos import enocontrar_contornos
from funciones.funciones_de_contorno import contorno_macro, calados_huerfanos, obtener_limites_contorno,normalizar_geometria_pieza


def procesar_pieza (ruta_dxf):
    '''
    Lee un archivo DXF individual, extrae sus geometrías, filtra la basura
    y devuelve un diccionario estructurado con la información de la pieza.
    '''
    try:
        doc = ezdxf.readfile(ruta_dxf)
        msp = doc.modelspace()
        segmentos = []

        for entity in msp:
                    entidad = entity.dxftype()

                    match entidad:
                        case 'LINE':
                            segmentos.append(linea(entity))
                        case 'ARC':
                            segmentos.append(arco(entity))
                        case 'SPLINE':
                            # Usamos .construction_tool() y el método .flattening(tolerancia) correcto
                            puntos_curva = list(entity.construction_tool().flattening(0.5))
                            
                            # Convertimos esos puntos en tus segmentos (inicio, fin)
                            for i in range(len(puntos_curva) - 1):
                                p1 = puntos_curva[i]
                                p2 = puntos_curva[i+1]
                                # Como puntos_curva devuelve objetos Vec3, accedemos a x e y directamente
                                segmentos.append(((p1.x, p1.y), (p2.x, p2.y)))

        contornos = enocontrar_contornos(segmentos)

        idx_macro = contorno_macro(contornos)
        perimetro_macro = contornos.pop(idx_macro)
        limites_macro = obtener_limites_contorno(perimetro_macro)

        posibles_calados = contornos
        calados_validos = calados_huerfanos(posibles_calados, limites_macro)

        limite_normalizado, contorno_macro_normalizado, contornos_calados_normalizados = normalizar_geometria_pieza(limites_macro, perimetro_macro, calados_validos)

        pieza_normalizada = {
            "archivo":ruta_dxf.name,
            "limites": limite_normalizado,
            "contorno_macro": contorno_macro_normalizado,
            "contornos_calados": contornos_calados_normalizados
        }

        pieza = {
            "archivo":ruta_dxf.name,
            "limites": limites_macro,
            "contorno_macro": perimetro_macro,
            "contornos_calados": calados_validos
        }

        return pieza_normalizada

    except IOError:
        print(f'Error: No se encontró o no se pudo abrir el archivo.')
        return None
    except ezdxf.DXFStructureError:
        print(f'Error: El archivo DXF está dañado o no es válido.')
        return None