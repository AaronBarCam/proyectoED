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
#def impClasificacion(lista):
#    equipos=[]
#    for i in lista:
#        equipos.append({
#            "equipo": i[1]
#        })

#    return equipos
datos = LeerPartidos()

#equipos= impClasificacion(datos)

# def Equipos(datosliga):

# def InfoEquipos(datosliga,equipos):

# def QuienGana(resultado):

# def Puntos(info):

# def Clasificacion(datos):
