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

equipos = LeerPartidos()


print(equipos)

#def impClasificacion(lista):


def Equipos(datosliga):
    equ

Equipos(equipos)


# def InfoEquipos(datosliga,equipos):


# def QuienGana(resultado):


# def Puntos(info):


# def Clasificacion(datos):
