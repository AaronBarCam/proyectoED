# Proyecto entornos de desarrollo

import csv


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

# def impClasificacion(lista):

datos = LeerPartidos()
for i in datos:
    print(i)

# equipos= impClasificacion(datos)

def Equipos(datosliga):

    equipos=[]
    liguilla=[]

    for i in datosliga:
<<<<<<< HEAD
        nombreEquipo = i[1]
        if nombreEquipo not in liguilla:
            liguilla.append(nombreEquipo)
            equipos.append({"equipos": nombreEquipo})

    return equipos

EquiposDatos = Equipos(datos)
for i in EquiposDatos:
=======
        if i[1] not in equipos:
            equipos.append(i[1])
    

    return equipos

equiposdatos = Equipos(datos)
for i in equiposdatos:
>>>>>>> 80cb9ec6cd054eed85d72b363712cad8860725dc
    print(i)

# def InfoEquipos(datosliga,equipos):

# def QuienGana(resultado):

# def Puntos(info):

# def Clasificacion(datos):
