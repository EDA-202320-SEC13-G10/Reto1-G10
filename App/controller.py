﻿"""
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
def tipo_sort(control,tipo):
    r =  control["model"]["results"]
    start_time =  get_time()
    model.sorter_date_country(r,tipo)
    end_time = get_time()
    delta = delta_time(start_time,end_time)
    return  r , delta

def load_data(control):
    
    """
    Carga los datos del reto
    """
    #TODO: Realizar la carga de datos
    dtos = control["model"]
    results = loadRasults(dtos)
    goalscorers  = loadGoalscorers(dtos)
    shootouts  = loadShootouts(dtos)
    return results , goalscorers , shootouts



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

def primeros_ultimos(control):
    return model.first_last3(control) 

# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control, pais, tipolocal, tamanio):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    result =  control["model"]["results"]
    rq1model = model.req_1(result , pais , tipolocal)
    size= model.data_size(rq1model)

    return  rq1model, size
    



def req_2(control, nombre, n):
    """
    Retorna el resultado del requerimiento 2
    """
    goalscorers = control["model"]["goalscorers"]
    rq2model = model.req_2(goalscorers, nombre)
    size = model.data_size(rq2model)
    return rq2model, size


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
