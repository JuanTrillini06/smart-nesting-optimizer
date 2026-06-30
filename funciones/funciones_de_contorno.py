def obtener_limites_contorno (contorno:list):
    lista_x = [punto[0] for punto in contorno]
    lista_y = [punto[1] for punto in contorno]
    return min(lista_x), max(lista_x), min(lista_y), max(lista_y)

def contorno_macro (contornos: list) -> int:
    area_maxima = 0
    for indice, contorno in enumerate(contornos):
        x_min, x_max, y_min, y_max = obtener_limites_contorno(contorno)
        area = (x_max - x_min) * (y_max - y_min)
        if area > area_maxima:
            area_maxima = area
            indice_macro = indice
    return indice_macro

def calados_huerfanos (contornos: list,limites_macro: list):
    x_min_p, x_max_p, y_min_p, y_max_p = limites_macro
    calados_validos = []

    for contorno in contornos:
        x_min_h, x_max_h, y_min_h, y_max_h = obtener_limites_contorno(contorno)
        if (x_min_h > x_min_p and x_max_h < x_max_p and y_min_h > y_min_p and y_max_h < y_max_p):
            calados_validos.append(contorno)
    return calados_validos
