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
def QuienGana(resultado):

    for i in datos:
        ganador = i[4]
        equipoGanador=ganador.split("-")

        if int(equipoGanador[0]) > int(equipoGanador[1]):
            print("gana local")
            print("pierde visitante")
            print("")

        elif int(equipoGanador[0]) < int(equipoGanador[1]):
            print("gana visitante")
            print("pierde local")
            print("")

        elif int(equipoGanador[0]) == int(equipoGanador[1]):
            print("empatan")
            print("")

QuienGana(datos)


# FUNCION Puntos
#--------------------------
# def Puntos(info):


# FUNCION Clasificacion
#--------------------------
# def Clasificacion(datos):
