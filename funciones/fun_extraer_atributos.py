import math

def linea (entidad):
    inicio = (entidad.dxf.start.x, entidad.dxf.start.y)
    fin = (entidad.dxf.end.x, entidad.dxf.end.y)
    return (inicio, fin)

def arco (entidad):
    centro = (entidad.dxf.center.x, entidad.dxf.center.y)
    radio = (entidad.dxf.radius)
    angulos = (math.radians(entidad.dxf.start_angle), math.radians(entidad.dxf.end_angle))
    inicio = (centro[0] + radio * math.cos(angulos[0]), centro[1] + radio * math.sin(angulos[0]))
    fin = (centro[0] + radio * math.cos(angulos[1]), centro[1] + radio * math.sin(angulos[1]))
    return (inicio, fin)