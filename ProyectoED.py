# Proyecto entornos de desarrollo

import csv

liga = {}
MatchList=[]

def LeerPartidos():
    global liga
    with open("liga.csv") as file:
        datos = csv.reader(file)
        next(datos)

        for data in datos:
            MatchList.append(data)
    
    liga=MatchList

def impClasificacion(lista):
    LeerPartidos()

    for i in lista:
        print(i)


    


impClasificacion(liga)
         
LeerPartidos()
impClasificacion(MatchList)         


# def Equipos(datosliga):

# def InfoEquipos(datosliga,equipos):

# def QuienGana(resultado):

# def Puntos(info):

# def Clasificacion(datos):
