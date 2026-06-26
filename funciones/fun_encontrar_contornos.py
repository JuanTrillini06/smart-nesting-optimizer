def redondear_punto(punto):
    return (round(punto[0], 2), round(punto[1], 2))

def enocontrar_contornos (segmentos:list) -> list:
    '''
    La funcion compara los segmentos encontrados para buscar coincidencias y describir contornos.

    Entrada:
        Lista de segmentos: segmentos Type: list
    Salida:
        Lista de contornos: contornos_encontrados Type: list
    '''

    contornos_encontrados = []
    while len(segmentos) > 0:
        primer_segmento = segmentos.pop(0)
        contorno_actual = [primer_segmento[0], primer_segmento[1]]
        punto_busqueda = redondear_punto(primer_segmento[1])

        conexion = True
        while conexion: 
            conexion = False
            for segmento in segmentos:
                if redondear_punto(segmento[0]) == punto_busqueda:
                    contorno_actual.append(redondear_punto(segmento[1]))
                    punto_busqueda = redondear_punto(segmento[1])
                    conexion = True
                    segmentos.remove(segmento)
                    break
                elif redondear_punto(segmento[1]) == punto_busqueda:
                    contorno_actual.append(redondear_punto(segmento[0]))
                    punto_busqueda = redondear_punto(segmento[0])
                    conexion = True
                    segmentos.remove(segmento)
                    break
        
        contornos_encontrados.append(contorno_actual)
    
    return (contornos_encontrados)
