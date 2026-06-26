import ezdxf
from funciones.fun_extraer_atributos import linea, arco
from funciones.fun_encontrar_contornos import enocontrar_contornos

try: 
    doc = ezdxf.readfile(r'.\files\00.C.TR.00342.dxf')

    msp = doc.modelspace()
    print(f'Archivo leido correctamente.')

    segmentos = []

    for entity in msp:
        entidad = entity.dxftype()

        match entidad:
            case 'LINE':
                segmentos.append(linea(entity))
            case 'ARC':
                segmentos.append(arco(entity))

    print(f'Se encontraron: {len(segmentos)} entidades')
    print(f'Se encontraron: {len(enocontrar_contornos(segmentos))} contornos')

except IOError:
    print(f'Error: No se encontró o no se pudo abrir el archivo.')
except ezdxf.DXFStructureError:
    print(f'Error: El archivo DXF está dañado o no es válido.')