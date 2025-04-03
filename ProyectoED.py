# Proyecto entornos de desarrollo

import csv

liga = {}
MatchList=[]

def LeerPartidos():

    with open("liga.csv") as file:
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