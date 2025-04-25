# Proyecto entornos de desarrollo

import csv

cabezal = "Nombre - PartidosGanados - PartidosPerdidos - PartidosEmpatados - Puntos"

# FUNCION LeerPartidos
#--------------------------
def LeerPartidos():
    MatchList=[]
    liga={}
    with open("liga.csv") as file:

        datos = csv.reader(file)
        next(datos)

        for data in datos:
            MatchList.append(data)
            
        liga=MatchList
        
    return liga

datos = LeerPartidos()

# FUNCION impClasificacion
#--------------------------
def impClasificacion(lista):

    equipos = Equipos(datos)
    InfoEquipos(datos, equipos)

# FUNCION Equipos
#--------------------------
def Equipos(datosliga):

    equipos=[]
    
    for i in datosliga:

        if i[1] not in equipos:
            equipos.append(i[1])   
    
    return equipos

equiposdatos = Equipos(datos)


# FUNCION InfoEquipos
#--------------------------
def InfoEquipos(datosliga,equipos):

    equipos_info = {equipo: [0, 0, 0, 0] for equipo in equipos}

    for partido in datosliga:
        equipo_local = partido[1]
        equipo_visitante = partido[2]
        resultado = QuienGana(partido[3])

        if resultado == 1:
            equipos_info[equipo_local][0] += 1
            equipos_info[equipo_local][3] += 3
            equipos_info[equipo_visitante][2] += 1

        elif resultado == -1:
            equipos_info[equipo_local][2] += 1
            equipos_info[equipo_visitante][0] += 1
            equipos_info[equipo_visitante][3] += 3
        
        elif resultado == 0:
            equipos_info[equipo_local][1] += 1
            equipos_info[equipo_visitante][1] += 1
            equipos_info[equipo_local][3] += 1
            equipos_info[equipo_visitante][3] += 1

    equipos_resultados = []

    for equipo, stats in equipos_info.items():
        equipos_resultados.append((equipo, stats[0], stats[1], stats[2], Puntos(stats)))
    

    Clasificacion(equipos_resultados)

# FUNCION QuienGana
#--------------------------
def QuienGana(resultado):

    e1, e2 = map(int, resultado.split("-"))
    
    if e1 > e2:
        return 1
    
    elif e1 < e2:
        return -1
    
    else:
        return 0 


# FUNCION Puntos
#--------------------------
def Puntos(info):

    partidos_ganados = info[0]
    partidos_empatados = info[1]
    
    puntos = (partidos_ganados * 3) + (partidos_empatados * 1)

    return puntos

# FUNCION Clasificacion
#--------------------------
def Clasificacion(datos):

    ordenado = sorted(datos, key=lambda item: item[4], reverse=True)

    for equipo, ganados, empatados, perdidos, puntos in ordenado:
        print(f"{equipo} - {ganados} - {empatados} - {perdidos} - {puntos}")


datos = LeerPartidos()
print(cabezal)
impClasificacion(datos)