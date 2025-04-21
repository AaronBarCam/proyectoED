# Proyecto entornos de desarrollo

import csv

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

    equiposdatos = Equipos(lista)

    print("EQUIPOS:")
    for i in equiposdatos:
        print(i)


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
# def InfoEquipos(datosliga,equipos):


# FUNCION QuienGana
#--------------------------
# def QuienGana(resultado):


# FUNCION Puntos
#--------------------------
def Puntos(info):

    ListaEquipos = {}

    for i in info:
        ganador = i[4]
        equipoGanador = ganador.split("-")

        equipo1 = i[1]
        equipo2 = i[2]
        
        if int(equipoGanador[0]) > int(equipoGanador[1]):
           
            if equipo1 not in ListaEquipos:
                ListaEquipos[equipo1] = 3
            else:
                ListaEquipos[equipo1] += 3
        
        elif int(equipoGanador[0]) < int(equipoGanador[1]):
        
            if equipo2 not in ListaEquipos:
                ListaEquipos[equipo2] = 3
            else:
                ListaEquipos[equipo2] += 3
        
        elif int(equipoGanador[0]) == int(equipoGanador[1]):
         
            if equipo1 not in ListaEquipos:
                ListaEquipos[equipo1] = 1
            else:
                ListaEquipos[equipo1] += 1

            if equipo2 not in ListaEquipos:
                ListaEquipos[equipo2] = 1
            else:
                ListaEquipos[equipo2] += 1

    return ListaEquipos

puntos = Puntos(datos)

# FUNCION Clasificacion
#--------------------------
def Clasificacion(datos):

    ordenado = dict(sorted(datos.items(), key=lambda item: item[1], reverse=True))

    for i, j in ordenado.items():
        print(f"{i} --> {j}")

Clasificacion(puntos)