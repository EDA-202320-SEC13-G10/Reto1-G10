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
 """

import config as cf
import model
import time
import csv
csv.field_size_limit(2147483647)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = {
        "model" : None
    }
    control["model"] = model.new_data_structs()
    return control


# Funciones para la carga de datos


def load_data(control):
    
    """
    Carga los datos del reto
    """
    #TODO: Realizar la carga de datos
    dtos = control["model"]
    results = loadRasults(dtos)
    goalscorers  = loadGoalscorers(dtos)
    shootouts  = loadShootouts(dtos)
    return model.sorter_date_country(results) , goalscorers , shootouts

def loadRasults(dtos):
    filename = "football/results-utf8-small.csv"
    file = cf.data_dir + filename
    input_file = csv.DictReader(open(file , encoding='utf-8'))
    for data in input_file:
        model.add_Results(dtos,data)
    return dtos["results"]


def loadGoalscorers(dtos):
    filename = "football/goalscorers-utf8-small.csv"
    file = cf.data_dir + filename
    input_file = csv.DictReader(open(file , encoding='utf-8'))
    for data in input_file:
        model.add_Goalscorers(dtos,data)
    return dtos["goalscorers"]


def loadShootouts(dtos):
    filename = "football/shootouts-utf8-small.csv"
    file = cf.data_dir + filename
    input_file = csv.DictReader(open(file , encoding='utf-8'))
    for data in input_file:
        model.add_Shootouts(dtos,data)
    return dtos["shootouts"]


# Funciones de ordenamiento

def sizedtos(control,posi):
    pos = control["model"]
    return model.data_size(pos[posi])

def primeros_ultimos(control, posi):
    dtos = control["model"]     
    return model.first_last3(dtos[posi]) 

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control, pais, tipolocal, n):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    x , y, z = load_data(control)
    
    h = model.req_1(x , pais , tipolocal )
    size= model.data_size(h)
    sublista = model.sublista(h,1,n)
    return sublista, model.data_size(sublista)
    



def req_2(control, nombre, n):
    """
    Retorna el resultado del requerimiento 2
    """
    x , y, z = load_data(control)
    h = model.req_2(y, nombre)
    s = model.data_size(h)
    if  n > 6:
        return model.first_last3(h) , s
    else:
        return model.sublista(h,(s+1)-s,s) , s
        


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
