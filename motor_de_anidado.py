from procesar_archivos import cargar_todas_las_piezas

carpeta_de_piezas = "./files"

lista_de_piezas = cargar_todas_las_piezas(carpeta_de_piezas)

chapa = {
    "ancho": 6000.0,
    "alto": 1510.0,
    "margen": 4.5,
    "piezas_reubicadas": [] # Aquí irán las piezas que logremos acomodar
}

# nesting_engine.py
def calcular_area_pieza(pieza):
    """Calcula el área del bounding box de la pieza."""
    x_min, x_max, y_min, y_max = pieza["limites"]
    ancho = x_max - x_min
    alto = y_max - y_min
    return ancho * alto

def ejecutar_nesting(lista_piezas, ancho_chapa=3000.0, alto_chapa=1500.0, margen=4.5, separacion=4.0):
    print("🚀 Iniciando Motor de Anidado (Nesting Engine)...")
    
    # 1. ORDENAMIENTO: Ordenamos las piezas de mayor a menor área
    piezas_ordenadas = sorted(lista_piezas, key=calcular_area_pieza, reverse=True)
    
    print(f"📊 {len(piezas_ordenadas)} piezas ordenadas por tamaño listas para acomodar.")
    
    # 2. DEFINICIÓN DEL CONTENEDOR (CHAPA)
    # Lista para almacenar las piezas que logremos ubicar con sus nuevas coordenadas
    piezas_colocadas = [] 
    
    # Lista de puntos candidatos (empezamos en la esquina inferior izquierda considerando el margen)
    puntos_candidatos = [(margen, margen)]
    
    # PADDING: El inflado que tendrá cada pieza por seguridad
    padding = separacion / 2.0
    
    # 3. BUCLE PRINCIPAL: Intentar colocar cada pieza una por una
    for pieza in piezas_ordenadas:
        x_min, x_max, y_min, y_max = pieza["limites"]
        ancho_real = x_max - x_min
        alto_real = y_max - y_min
        
        # El tamaño virtual que ocupa en la chapa con la distancia de seguridad
        ancho_ocupado = ancho_real + (2 * padding)
        alto_ocupado = alto_real + (2 * padding)
        
        pieza_ubicada = False
        
        # Aquí recorreremos los puntos_candidatos ordenados (de abajo-izquierda a arriba-derecha)
        # para ver en cuál de ellos entra la pieza sin colisionar con las anteriores
        # ... (Próximo paso: Algoritmo de colisión y selección de punto)
        
    return piezas_colocadas

def hay_colision(x_cand, y_cand, ancho_o, alto_o, piezas_colocadas):
    """
    Evalúa si un rectángulo virtual en la posición (x_cand, y_cand)
    colisiona con alguna de las piezas que ya fueron ubicadas en la chapa.
    """
    # Definimos las fronteras de la pieza que queremos colocar
    izq1 = x_cand
    der1 = x_cand + ancho_o
    aba1 = y_cand
    arr1 = y_cand + alto_o
    
    for pieza in piezas_colocadas:
        # Recuperamos la posición donde fue colocada la pieza anterior
        # (Necesitaremos guardar 'x_ubicada' e 'y_ubicada' al empaquetarla)
        izq2 = pieza["x_ubicada"]
        der2 = pieza["x_ubicada"] + pieza["ancho_ocupado"]
        aba2 = pieza["y_ubicada"]
        arr2 = pieza["y_ubicada"] + pieza["alto_ocupado"]
        
        # Condición de superposición de rectángulos
        if not (der1 <= izq2 or izq1 >= der2 or arr1 <= aba2 or aba1 >= arr2):
            return True  # ¡Hay colisión! Se están superponiendo
            
    return False  # No colisiona con ninguna pieza colocada

if __name__ == "__main__":
    # Esto es solo para probar el módulo de forma aislada importando tus 26 piezas procesadas
    # Suponiendo que traemos 'todas_las_piezas' de tu script anterior:
    pass