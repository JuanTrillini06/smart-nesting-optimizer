from pathlib import Path
from encontrar_entidades import procesar_pieza

def cargar_todas_las_piezas(carpeta_origen):
    ruta_carpeta = Path(carpeta_origen)
    lista_de_piezas = []
    
    # Usamos set() al sumar para eliminar automáticamente cualquier archivo duplicado, y luego lo hacemos lista
    archivos_dxf = list(set(ruta_carpeta.glob("*.dxf")) | set(ruta_carpeta.glob("*.DXF")))
    
    print(f"📋 Se encontraron {len(archivos_dxf)} archivos DXF para procesar.\n")
    
    for archivo in archivos_dxf:
        # Llamamos a la función modularizada
        datos_pieza = procesar_pieza(archivo)
        
        if datos_pieza:
            lista_de_piezas.append(datos_pieza)
        else:
            print(f"⚠️ Se omitió el archivo {archivo.name} debido a errores.")
            
    return lista_de_piezas

if __name__ == "__main__":
    # Definimos la ruta de la carpeta de archivos
    carpeta_files = "./files"
    
    # Ejecutamos el lote completo
    todas_las_piezas = cargar_todas_las_piezas(carpeta_files)
    
    print("\n--- RESUMEN DEL PROCESAMIENTO ---")
    print(f"📦 Total de piezas listas para Nesting: {len(todas_las_piezas)}")
    for pieza in todas_las_piezas:
        print(f'{pieza}\n')

