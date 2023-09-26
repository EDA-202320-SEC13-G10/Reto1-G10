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
    dtos["results"] = lt.newList("ARRAY_LIST")
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


def sorter_date_country(control):
    merg.sort(control,cmp_partidos_by_fecha_y_pais)
    return control

def sublista(data_structs, pos_i, num):
    s =  lt.subList(data_structs, pos_i, num)
    return s



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
        if i[tipolocal].lower() == pais.lower():
            lt.addLast(nl, i)
    return nl

def req_2(data_structs , nombre):
    """
    Función que soluciona el requerimiento 2
    """
    nl= lt.newList("ARRAY_LIST")
    for i in lt.iterator(data_structs):
        if i["scorer"] == nombre:
            lt.addLast(nl,i)
    return nl



def req_3(data_structs, date_i, date_f , team):
    """
    Función que soluciona el requerimiento 3
    """
    results = data_structs["model"]["results"]
    goalscorers = data_structs["model"]["goalscorers"]
    first = time.strptime(date_i, "%Y-%m-%d")
    second = time.strptime(date_f, "%Y-%m-%d")
    nl= lt.newList("ARRAY_LIST")
    home_matchs = 0
    away_matchs = 0
    for i in lt.iterator(results):
        date_actual = time.strptime(i["date"], "%Y-%m-%d")
        if date_actual > first and date_actual < second:
                    if i["home_team"].lower() == team.lower()or i["away_team"].lower() == team.lower():
                        if i["home_team"].lower() == team.lower():
                            home_matchs += 1
                        else:
                            away_matchs += 1
                        lt.addLast(nl,i)
    ne= lt.newList("ARRAY_LIST")
    for i in lt.iterator(nl):
        x = {}
        for j in lt.iterator(goalscorers):
            if i["date"] == j["date"]:
                if ["home_team"] == j["home_team"]:
                    x["date"] = j["date"]
                    x["home_team"] = j["home_team"]
                    x["away_team"] = j["away_team"]
                    x["home_score"] = i["home_score"]
                    x["away_score"] = i["away_score"]
                    x["country"] = i["country"]
                    x["city"] = i["city"]
                    x["tournament"] = i["tournament"]
                    x["penalty"] = j["penalty"]
                    x["own_goal"] = j["own_goal"]
                    lt.addLast(ne,x)
    # TODO: Realizar el requerimiento 3
    
    return ne, home_matchs, away_matchs


    


def req_4(data_structs, date_i, date_f, tournament):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 5
    results = data_structs["model"]["results"]
    shootouts = data_structs["model"]["shootouts"]
    first = time.strptime(date_i, "%Y-%m-%d")
    second = time.strptime(date_f, "%Y-%m-%d")
    nl= lt.newList("ARRAY_LIST")
    matches = 0
    shootout = 0
    ct = []
    cou = []
    for i in lt.iterator(results):
        date_actual = time.strptime(i["date"], "%Y-%m-%d")
        if date_actual > first and date_actual < second:
            if i["tournament"].lower() == tournament.lower():
                matches += 1
                lt.addLast(nl,i)
                if not(i["city"].lower()) in ct:
                    ct.append(i["city"].lower())
                if not(i["country"].lower()) in cou:
                    cou.append(i["country"].lower())
    cities = len(ct)
    countries = len(cou)
    ne= lt.newList("ARRAY_LIST")
    for i in lt.iterator(nl):
        pen = "Unknown"
        x = {}
        for j in lt.iterator(shootouts):
            if i["date"] == j["date"]:
                if i["home_team"] == j["home_team"]:
                    pen = j["winner"]
                    shootout += 1
        x["date"] = i["date"]
        x["tournament"] = i["tournament"]
        x["country"] = i["country"]
        x["city"] = i["city"]
        x["home_team"] = i["home_team"]
        x["away_team"] = i["away_team"]
        x["home_score"] = i["home_score"]
        x["away_score"] = i["away_score"]
        x["winner"] = pen
        lt.addLast(ne, x)
        
    return ne, matches, countries, cities, shootout
                
                
    

def req_5(data_structs, date_i, date_f , nombre):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 4
    results = data_structs["model"]["results"]
    goalscorers = data_structs["model"]["goalscorers"]
    first = time.strptime(date_i, "%Y-%m-%d")
    second = time.strptime(date_f, "%Y-%m-%d")
    nl= lt.newList("ARRAY_LIST")
    penalty = 0
    own_goal = 0
    for i in lt.iterator(goalscorers):
        date_actual = time.strptime(i["date"], "%Y-%m-%d")
        if date_actual > first and date_actual < second:
                    if i["scorer"].lower() == nombre.lower():
                        if i["penalty"] == "True":
                            penalty += 1
                        if i["own_goal"] == "True":
                            own_goal += 1
                        lt.addLast(nl,i)
    return nl, penalty, own_goal                     


def req_6(data_structs , tamanio,  date_i, date_f, torneo):

    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    results =sorter_date_country(data_structs["model"]["results"])
    goalscorers = data_structs["model"]["goalscorers"]
    nl =  lt.newList("ARRAY_LIST")
    first = time.strptime(date_i, "%Y-%m-%d")
    second = time.strptime(date_f, "%Y-%m-%d")
    for i in lt.iterator(results):
        date_actual = time.strptime(i["date"], "%Y-%m-%d")
        if date_actual > first and date_actual < second:
            if i["tournament"] == torneo:
                lt.addLast(nl,i)


def paises(data_structs):
    teams = lt.newList("ARRAY_LIST")
    for i in lt.iterator(data_structs):
         if lt.isPresent(teams,i["team"]) == 0:
             lt.addLast(teams,i["team"])
    merg.sort(teams,cmp_teams)
    return teams

def scorer_names(data_structs):
    scorer_name = lt.newList("ARRAY_LIST")
    for i in lt.iterator(data_structs):
         if lt.isPresent(scorer_name,i["scorer"]) == 0:
             lt.addLast(scorer_name,i["scorer"])
    return scorer_name

def top_scorer(data_structs): 
    scorer = lt.newList("ARRAY_LIST")
    scorers = data_structs["model"]["goalscorers"]
    pais= paises(scorers)
    scorer_name = scorer_names(scorers)
    for i in lt.iterator(pais):
        x = {}
        x[i] = lt.newList("ARRAY_LIST")
        for j in lt.iterator(scorers):
            if i == j["team"]:
                lt.addLast(x[i],j)
        lt.addLast(scorer,x[i])
           
    return  scorer

def req_7(data_structs, tamanio,  date_i, date_f):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    results = data_structs["model"]["results"]
    scorers = data_structs["model"]["goalscorers"]
    first = time.strptime(date_i, "%Y-%m-%d")
    second = time.strptime(date_f, "%Y-%m-%d")
    x = {}
    penalties = 0
    own_goals = 0
    goals = 0
    mat = []
    h = 0 # Para indicar goles
    for i in lt.iterator(scorers):
        date_actual = time.strptime(i["date"], "%Y-%m-%d")
        if date_actual > first and date_actual < second:
            for j in lt.iterator(results):
                fecha = time.strptime(j["date"], "%Y-%m-%d")
                if fecha == date_actual:
                    if i["home_team"].lower() == j["home_team"].lower():
                        # Cantidad de partidos y goles (revisión)
                        if not([j["date"], j["home_team"]]) in mat:
                            mat.append([j["date"], j["home_team"]])
                            goals += (int(j["home_score"]) + int(j["away_score"]))
                        # Estadisticas goleadores 
                        if not(i["scorer"]) in x.keys():
                            x[i["scorer"]] = [0,0,0,0,[],[],0,0,0,[]]
                        # Goles, autogoles, penaltys y puntos
                        x[i["scorer"]][1] += 1
                        if i["own_goal"] == "True":
                            x[i["scorer"]][3] += 1
                            x[i["scorer"]][0] -= 1
                            own_goals += 1
                        elif i["penalty"] == "True":
                            x[i["scorer"]][2] += 1
                            x[i["scorer"]][0] += 2
                            penalties += 1
                        else:
                            x[i["scorer"]][0] += 1
                        # Promedio de minutos
                        x[i["scorer"]][4].append(float(i["minute"]))
                        # Torneos
                        if not(j["tournament"].lower()) in x[i["scorer"]][5]:
                            x[i["scorer"]][5].append(j["tournament"].lower())
                        # Goles anotados en victoria, derrota o empate
                        if i["team"].lower() == j["home_team"].lower() and j["home_score"] > j["away_score"]:
                            x[i["scorer"]][6] += 1
                        elif i["team"].lower() == j["home_team"].lower() and j["home_score"] == j["away_score"]:
                            x[i["scorer"]][8] += 1
                        elif i["team"].lower() == j["home_team"].lower() and j["home_score"] < j["away_score"]:
                            x[i["scorer"]][7] += 1
                        elif i["team"].lower() == j["away_team"].lower() and j["home_score"] > j["away_score"]:
                            x[i["scorer"]][7] += 1
                        elif i["team"].lower() == j["away_team"].lower() and j["home_score"] == j["away_score"]:
                            x[i["scorer"]][8] += 1
                        elif i["team"].lower() == j["away_team"].lower() and j["home_score"] < j["away_score"]:
                            x[i["scorer"]][6] += 1
                        # Ultimo gol
                        x[i["scorer"]][9] = {"date": j["date"], "tournament": j["tournament"], "home_team": j["home_team"], "away_team": j["away_team"], "home_score": j["home_score"], "away_score": j["away_score"], "minute": i["minute"], "penalty": i["penalty"], "own_goal": i["own_goal"]}
    nl = lt.newList("ARRAY_LIST")
    sco_names = list(x.keys())
    sco_values = list(x.values())
    players = 0
    matches = len(mat)
    # Organizar
    for sc in range(len(x)):
        gs = {}
        gs["scorer"] = sco_names[sc]
        gs["total_points"] = sco_values[sc][0]
        gs["total_goals"] = sco_values[sc][1]
        gs["penalty_goals"] = sco_values[sc][2]
        gs["own_goals"] = sco_values[sc][3]
        gs["avg_time [min]"] = sum(sco_values[sc][4])/len(sco_values[sc][4])
        gs["total_tournaments"] = len(sco_values[sc][5])
        gs["scored_in_wins"] = sco_values[sc][6]
        gs["scored_in_losses"] = sco_values[sc][7]
        gs["scored_in_draws"] = sco_values[sc][8]
        ne = lt.newList("ARRAY_LIST")
        gs["last_goal"] = lt.addLast(ne,sco_values[sc][9])
        players += 1
        lt.addLast(nl,gs)
    # Sort
    # Sublist con N
    nl = lt.subList(nl,1,tamanio)
    return nl, players, matches, goals, penalties, own_goals
    

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
def cmp_partidos_by_fecha_y_pais (data_1,  data_2):
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



def compare_dates_inter(data_1,  data_2):
    x = (data_1["date"])
    y = (data_2["date"])
    first = time.strptime(x, "%Y-%m-%d")
    second = time.strptime(y, "%Y-%m-%d")
    return first < second



def cmp_teams(data_1,  data_2):
    return data_1 < data_2




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
