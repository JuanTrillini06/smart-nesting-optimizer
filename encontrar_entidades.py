import ezdxf
from funciones.fun_extraer_atributos import linea, arco
from funciones.fun_encontrar_contornos import enocontrar_contornos
from funciones.funciones_de_contorno import contorno_macro, calados_huerfanos, obtener_limites_contorno


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

        contornos = enocontrar_contornos(segmentos)

        idx_macro = contorno_macro(contornos)
        perimetro_macro = contornos.pop(idx_macro)
        limites_macro = obtener_limites_contorno(perimetro_macro)

        posibles_calados = contornos
        calados_validos = calados_huerfanos(posibles_calados, limites_macro)

        return {
            "archivo":ruta_dxf.name,
            "limites": limites_macro,
            "contorno_macro": perimetro_macro,
            "contornos_calados": calados_validos
        }

    except IOError:
        print(f'Error: No se encontró o no se pudo abrir el archivo.')
        return None
    except ezdxf.DXFStructureError:
        print(f'Error: El archivo DXF está dañado o no es válido.')
        return None