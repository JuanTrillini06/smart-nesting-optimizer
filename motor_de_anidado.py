from procesar_archivos import cargar_todas_las_piezas
from funciones.funciones_de_contorno import calcular_area_pieza

carpeta_de_piezas = "./files"

lista_de_piezas = cargar_todas_las_piezas(carpeta_de_piezas)

SEPARACION = 4.0
padding = SEPARACION / 2  # Da 2.0 mm

chapa = {
    "ancho": 6000.0,
    "alto": 1510.0,
    "margen": 4.5,
    "piezas_reubicadas": [] # Aquí irán las piezas que logremos acomodar
}

def motor_nesting(chapa, padding, lista_piezas):
    # El primer punto candidato arranca en (2.5, 2.5) para lograr el solapamiento perfecto
    puntos_candidatos = [(chapa['margen'] - padding, chapa['margen'] - padding)]
    piezas_fuera = []

    for pieza in lista_piezas:
        # IMPORTANTE: El "bloque virtual ocupado" es el tamaño real + padding de ambos lados (izq/der o arriba/abajo)
        ancho_ocupado = pieza['limites'][1] + (2 * padding)
        alto_ocupado = pieza['limites'][3] + (2 * padding)
        
        pieza_colocada_con_exito = False
        
        # Recorremos la lista de puntos candidatos que tenemos hasta el momento
        for x_cand, y_cand in puntos_candidatos:
            
            # El rectángulo virtual ocupado se proyecta desde el punto candidato
            x_ini = x_cand
            y_ini = y_cand
            x_fin = x_cand + ancho_ocupado
            y_fin = y_cand + alto_ocupado
            
            # FILTRO 1: Condición de frontera de la chapa
            if x_fin <= chapa['ancho'] and y_fin <= chapa['alto']:
                
                # FILTRO 2: Condición de colisión contra las piezas ya ubicadas en la chapa
                colisiona = False
                for lpu in chapa['piezas_reubicadas']:

                    if not (x_ini >= lpu['x_fin'] or x_fin <= lpu['x_ini'] or y_ini >= lpu['y_fin'] or y_fin <= lpu['y_ini']):
                        colisiona = True
                        break
                
                if not colisiona:

                    chapa['piezas_reubicadas'].append({
                        "archivo": pieza['archivo'],
                        "x_ini": x_ini,
                        "y_ini": y_ini,
                        "x_fin": x_fin,
                        "y_fin": y_fin,
                        "contorno_macro": pieza['contorno_macro'],
                        "contornos_calados": pieza['contornos_calados']
                    })
                    
                    puntos_candidatos.extend([(x_ini,y_fin),(x_fin,y_fin),(x_fin,y_ini)])

                    puntos_candidatos = list(set(puntos_candidatos))
                    puntos_candidatos = sorted(puntos_candidatos, key=lambda p: (p[1], p[0]))
                    
                    pieza_colocada_con_exito = True
                    break

        if not pieza_colocada_con_exito:
            piezas_fuera.append(pieza['archivo'])

    return chapa['piezas_reubicadas'], piezas_fuera

if __name__ == "__main__":
    print("🚀 Iniciando el motor de Nesting Bottom-Left...")
    print(f"📦 Total de piezas cargadas: {len(lista_de_piezas)}")
    print("-" * 50)
    
    ubicadas, afuera = motor_nesting(chapa, padding, lista_de_piezas)
    
    print("\n✅ REPORTE DE ACOMODO:")
    print(f"🧩 Piezas reubicadas con éxito: {len(ubicadas)}")
    for i, p in enumerate(ubicadas, 1):
        # Le restamos el padding al reporte visual para ver dónde arranca la pieza REAL
        print(f"  {i}. [{p['archivo']}] -> Ubicada en X: {p['x_ini']+padding:.1f}, Y: {p['y_ini']+padding:.1f}")
        
    if afuera:
        print(f"\n❌ Piezas que NO entraron ({len(afuera)}):")
        for p in afuera:
            print(f"  - {p}")
    else:
        print("\n🎉 ¡Espectacular! Todas las piezas entraron perfectamente en la chapa.")