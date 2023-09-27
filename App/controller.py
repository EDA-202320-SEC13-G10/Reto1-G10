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
    filename = "football/results-utf8-30pct.csv"
    file = cf.data_dir + filename
    input_file = csv.DictReader(open(file , encoding='utf-8'))
    for data in input_file:
        model.add_Results(dtos,data)
    return dtos["results"]



def loadGoalscorers(dtos):
    filename = "football/goalscorers-utf8-30pct.csv"
    file = cf.data_dir + filename
    input_file = csv.DictReader(open(file , encoding='utf-8'))
    for data in input_file:
        model.add_Goalscorers(dtos,data)
    return dtos["goalscorers"]


def loadShootouts(dtos):
    filename = "football/shootouts-utf8-30pct.csv"
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


def req_1(control, pais, tipolocal, n):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    result =  control["model"]["results"]
    start=get_time()
    rq1model = model.req_1(result , pais , tipolocal)
    end=get_time()
    tiempo=delta_time(start,end)
    size= model.data_size(rq1model)
    size_i = size
    if size > n:
        size = n
        rq1model =  model.sublista(rq1model,1,size)
    
    if size > 6:
        rq1model =  model.first_last3(rq1model)
    return  rq1model, size ,size_i, tiempo

    


def req_2(control, nombre, n):
    """
    Retorna el resultado del requerimiento 2
    """
    goalscorers = control["model"]["goalscorers"]
    start=get_time()
    rq2model = model.req_2(goalscorers, nombre)
    end=get_time()
    tiempo=delta_time(start,end)
    size = model.data_size(rq2model)
    size_i = size
    if size > n:
        size = n
    rq2model =  model.sublista(rq2model,1,size)
    if size < 6:
        rq2model =  rq2model
    else:
        rq2model =  model.first_last3(rq2model)

    return rq2model, size, size_i, tiempo


def req_3(control,date_i, date_f , team):
    """
    Retorna el resultado del requerimiento 3
    """
    start = get_time()
    dtos, home_matchs, away_matchs =  model.req_3(control,date_i, date_f , team)
    end = get_time()
    tiempo=delta_time(start,end)
    # TODO: Modificar el requerimiento 3
    total = home_matchs + away_matchs
    size = model.data_size(dtos)
    
    if size < 6:
        dtos =  dtos
    else:
        dtos =  model.first_last3(dtos)
    return dtos, home_matchs, away_matchs, total,size, tiempo


def req_4(control, date_i, date_f, tournament):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    start=get_time()
    nl, matches, countries, cities, shootouts = model.req_4(control, date_i, date_f, tournament)
    end=get_time()
    tiempo=delta_time(start,end)
    size = model.data_size(nl)
    
    return nl, matches, countries, cities, shootouts, size, tiempo


def req_5(control, date_i, date_f , nombre):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    start=get_time()
    nl, penalty, own_goal,goals  = model.req_5(control, date_i, date_f , nombre)
    end=get_time()
    tiempo=delta_time(start,end)
    size = model.data_size(nl)

    return nl, penalty, own_goal, goals, size, tiempo

def req_6(control,date_i, date_f, torneo,n):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    start=get_time()
    u ,n_teams, n_partidos,n_paises,n_ciudades = model.req_6(control,date_i, date_f, torneo)
    end=get_time()
    tiempo=delta_time(start,end)
    size = model.data_size(u)
    size_i = size
    if size > n:
        size = n
        u =  model.sublista(u,1,size)
    if size < 6:
        u =  u
    else:
        u =  model.first_last3(u)
    return  u ,n_teams, n_partidos,n_paises,n_ciudades, size_i, tiempo


def req_7(control, tamanio,  date_i, date_f):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    start=get_time()
    nl, players, matches, goals, penalties, own_goals = model.req_7(control, tamanio,  date_i, date_f)
    end=get_time()
    tiempo=delta_time(start,end)
    size = model.data_size(nl)
    size_i = size
    return nl, players, matches, goals, penalties, own_goals, size_i, tiempo

def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    start=get_time()
    z,x = model.req_8(control,"1952-03-25","2021-11-23","Argentina","Chile")
    end=get_time()
    tiempo=delta_time(start,end)
    return z , x, tiempo

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
