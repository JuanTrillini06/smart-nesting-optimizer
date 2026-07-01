def obtener_limites_contorno (contorno:list):
    lista_x = [punto[0] for punto in contorno]
    lista_y = [punto[1] for punto in contorno]
    return min(lista_x), max(lista_x), min(lista_y), max(lista_y)

def calcular_area_pieza(pieza):
    """Calcula el área del bounding box de la pieza."""
    x_min, x_max, y_min, y_max = pieza["limites"]
    ancho = x_max - x_min
    alto = y_max - y_min
    area = ancho * alto
    return area

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

def normalizar_geometria_pieza(limites, perimetro_macro, contornos_calados):
    # 1. Desempaquetamos los mínimos globales que usaremos para restar
    x_min_global, x_max_global, y_min_global, y_max_global= limites
    
    # 2. Nivel 1: Para el macrocontorno (un solo bucle for)
    macro_normalizado = []
    for punto in perimetro_macro:
        x_calc = punto[0] - (x_min_global)
        y_calc = punto[1] - (y_min_global)
        macro_normalizado.append((x_calc,y_calc))
        pass

    # 3. Nivel 2: Para los calados (dos bucles for anidados, tal como dijiste)
    calados_normalizados = []
    for calado in contornos_calados:
        nuevo_calado = []
        for punto in calado:
            x_calc = punto[0] - (x_min_global)
            y_calc = punto[1] - (y_min_global)
            nuevo_calado.append((x_calc,y_calc))
            pass
        calados_normalizados.append(nuevo_calado)
    
    # 4. Nivel 3: Calculo de los limites
    x_max_nuevo = x_max_global - x_min_global
    y_max_nuevo = y_max_global - y_min_global
    limites_normalizados = (0.0,x_max_nuevo,0.0,y_max_nuevo)
        
    return limites_normalizados, macro_normalizado, calados_normalizados
