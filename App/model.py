"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    
    dtos = {
        "results": None,
        "goalscorers" : None,
        "shootouts" : None
            }
    dtos["results"] = lt.newList('ARRAY_LIST')
    dtos["goalscorers"] = lt.newList('ARRAY_LIST')
    dtos["shootouts"] = lt.newList('ARRAY_LIST')

    return dtos


# Funciones para agregar informacion al modelo

def add_Results(data_structs,data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos
    lt.addLast(data_structs["results"],data)
    return data_structs
# Funciones para creacion de datos

def add_Goalscorers(data_structs,data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos
    lt.addLast(data_structs["goalscorers"],data)
    return data_structs


def add_Shootouts(data_structs,data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos
    lt.addLast(data_structs["shootouts"],data)
    return data_structs

def sorter_date_country(data_structs):
    merg.sort(data_structs,compare_dates)


def sublista(data_structs, pos_i, num):
    sublista =  lt.subList(data_structs, pos_i, num)
    return sublista



def first_last3(data_structs):
    primeros = sublista(data_structs,1,3)
    ultimos = sublista(data_structs,data_size(data_structs)-2,3)
    for i in lt.iterator(ultimos):
        lt.addLast(primeros,i)
    return primeros



def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass



# Funciones de consulta
def get_data_pos(data_structs,pos):
    data = lt.getElement(data_structs,pos)
    return data



def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass



def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    return lt.size(data_structs)



def req_1(data_structs, pais, tipolocal ) :
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    nl= lt.newList("ARRAY_LIST")
    if tipolocal.lower() == "home":
        tipolocal = "home_team"
    else:
        tipolocal = "away_team"
    for i in lt.iterator(data_structs):
        x= {}
        if i[tipolocal].lower() == pais:
            x["date"] = i["date"] 
            x["home_team"] = i["home_team"] 
            x["away_team"] = i["away_team"] 
            x["home_score"] = i["home_score"] 
            x["away_score"] = i["away_score"] 
            x["country"] = i["country"] 
            x["city"] = i["city"] 
            x["tournament"] = i["tournament"] 
            lt.addLast(nl, x)
    return nl

    

def req_2(data_structs , nombre):
    """
    Función que soluciona el requerimiento 2
    """
    nl= lt.newList("ARRAY_LIST")
    
    for i in lt.iterator(data_structs):
        x= {}
        if i["scorer"].lower() == nombre.lower():
            x["date"] = i["date"] 
            x["home_team"] = i["home_team"] 
            x["away_team"] = i["away_team"]     
            x["team"] = i["team"]     
            x["scorer"] = i["scorer"]     
            x["minute"] = i["minute"]     
            x["own_goal"] = i["own_goal"]     
            x["penalty"] = i["penalty"]     
            lt.addLast(nl, x)
    return nl



def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista


def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento
def compare_dates(data_1,  data_2):
    pos = True
    x = (data_1["date"])
    y = (data_2["date"])
    first = time.strptime(x, "%Y-%m-%d")
    second = time.strptime(y, "%Y-%m-%d")
    if first > second:
        if data_1["country"] > data_2["country"] :
            pos = True
    else:
        pos =  False
    return pos
def compare_dates2(data_1,  data_2):
    x = (data_1["date"])
    y = (data_2["date"])
    first = time.strptime(x, "%Y-%m-%d")
    second = time.strptime(y, "%Y-%m-%d")
    return first < second

    
    
def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
