# Proyecto entornos de desarrollo

import csv

liga = {}
MatchList=[]

def LeerPartidos():
<<<<<<< HEAD
   with open("liga.csv") as file:
=======

    with open("liga.csv") as file:
>>>>>>> 4734e618ba86666ba3fb397f0f46a98ee9c3e32d
        datos = csv.reader(file)
        next(datos)

        for data in datos:
            MatchList.append(data)
            liga=MatchList

def impClasificacion(lista):

    for i in lista:
        liga=lista

    print(liga)

LeerPartidos()
impClasificacion(MatchList)         
<<<<<<< HEAD
equipos(liga)
=======


# def Equipos(datosliga):

# def InfoEquipos(datosliga,equipos):

# def QuienGana(resultado):

# def Puntos(info):

# def Clasificacion(datos):
>>>>>>> 4a80979fda5626772ada90fdb2bc1df7e9721ec7
