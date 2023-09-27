"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
import tabulate as tb

assert cf
import traceback

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    control =  controller.new_controller()
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("10- Define el tipo de de lista en la estructura.")
    print("0- Salir")


def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    result, goalscorers, shootouts= controller.load_data(control) 
    return result, goalscorers, shootouts

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass
def print_carga(control):
    """
        Función que imprime la soluci1ón del Requerimiento 1 en consola
        Imprime los 3 primeros y los 3 ultimos cargados de los 3 archivos .

        control: la estrcutura de datos a cargar.
    """   
    # TODO: Imprimir el resultado del requerimiento 1

    rt = controller.sizedtos(control,"results")
    gl = controller.sizedtos(control,"goalscorers")
    sh = controller.sizedtos(control,"shootouts")

    l1 = controller.primeros_ultimos(control["model"]["results"])
    l2= controller.primeros_ultimos(control["model"]["goalscorers"])
    l3 = controller.primeros_ultimos(control["model"]["shootouts"])

    print(('Match results count: ' + str(rt)).center(130))
    print(('Goal scorers count: ' + str(gl)).center(130))
    print(('Shootouts-penalty definition count: ' + str(sh)).center(130))
    print("".center(130,"-"))
    print("".center(130,"="))
    print("FIFA RECORDS REPORT".center(130,"="))
    print("".center(130,"="))

    print("Print results for the first 3 and 3 last records on file.\n".center(130))
    
    print("".center(130,"-"))
    print("MATCH RESULTS".center(130,"-"))
    print("".center(130,"-"))
    print("         Total match results: " +str(rt))
    print("Results struct has more than 6 records...")
    print(tb.tabulate(l1["elements"] , headers = "keys" , tablefmt='grid'))
    
    print("".center(130,"-"))
    print("GOAL SCORERS".center(130,"-"))
    print("".center(130,"-"))
    print("         Total goal scorers: " +str(gl))
    print("Results struct has more than 6 records...")
    print(tb.tabulate(l2["elements"], headers = "keys" , tablefmt='grid'))
    
    print("".center(130,"-"))
    print("SHOOTOUTS".center(130,"-"))
    print("".center(130,"-"))
    print("         Total shootouts: " +str(sh))
    print("Results struct has more than 6 records...")
    print(tb.tabulate(l3["elements"], headers = "keys" , tablefmt='grid'))




def print_req_1(control):
    print("Req No. 1 Input".center(130,"="))

    n =  int(input("Number of matches: "))
    team_name =  input("Team name: ")
    tipolocal =  input("Team condition: ")

    print("Req No. 1 Results".center(130,"="))
    l1,l2, l3=controller.req_1(control,team_name,tipolocal,n)
    print(("Total matches found "+ str(l3)).center(100))
    print(("Selecting "+ str(l2) + " matches...").center(100))
    if l3 > 6:
        print("Resultrs struct has more than 6 records...")
    else:
        print("Resultrs struct has less than 6 records...")
    print(tb.tabulate(l1["elements"], headers = "keys" , tablefmt='grid'))
    print(l2)
    
    
def print_req_2(control ):
    """
        Función que imprime la solución del Requerimiento 2 
        en consola
    """
    print("Req No. 2 Input".center(130,"="))

    n =  int(input("Number of scorer: "))
    nombre =  input("Player name: ")
    l1,l2, l3=controller.req_2(control,nombre,n)
    print("Req No. 2 Results".center(130,"="))
    print(("Total matches found "+ str(l3)).center(100))
    print(("Selecting "+ str(l2) + " matches...").center(100))
    if l3 > 6:
        print("Resultrs struct has more than 6 records...")
    else:
        print("Resultrs struct has less than 6 records...")
    print(tb.tabulate(l1["elements"], headers = "keys", tablefmt='grid'))
    print(l2)
    


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    print("Req No. 3 Input".center(130,"="))

    team_name =  input("Team name: ")
    star_date =  input("Start date: ")
    end_date =  input("End date: ")
    dtos, home_matchs, away_matchs, total, size = controller.req_3(control,star_date, end_date , team_name)
    print("Req No. 3 Results".center(130,"="))
    print((team_name + " Total games "+ str(total)).center(100))
    print((team_name + " Total home games "+ str(home_matchs)).center(100))
    print((team_name + " Total away games "+ str(away_matchs)).center(100))

    if size > 6:
        print("Resultrs struct has more than 6 records...")
    else:
        print("Resultrs struct has less than 6 records...")
    print(tb.tabulate(dtos["elements"], headers = "keys" , tablefmt='grid'))


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 41
    
    print("Req No. 4 Input".center(130,"="))

    tournamnet_name =  input("Tournamnet name: ")
    star_date =  input("Start date: ")
    end_date =  input("End date: ")
    dtos, matches, countries, cities, shootouts, size = controller.req_4(control, star_date, end_date, tournamnet_name)
    print("Req No. 3 Results".center(130,"="))
    print((tournamnet_name + " Total matches "+ str(matches)).center(100))
    print((tournamnet_name + " Total countries "+ str(countries)).center(100))
    print((tournamnet_name + " Total cities "+ str(cities)).center(100))
    print((tournamnet_name + " Total cities "+ str(shootouts)).center(100))

    if size > 6:
        print("Resultrs struct has more than 6 records...")
    else:
        print("Resultrs struct has less than 6 records...")
    print(tb.tabulate(dtos["elements"], headers = "keys" , tablefmt='grid'))



def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    print("Req No. 5 Input".center(130,"="))

    player_name =  input("Player name: ")
    star_date =  input("Start date: ")
    end_date =  input("End date: ")
    dtos, penalty, own_goal,goals, size =  controller.req_5(control, star_date, end_date , player_name)
    print("Req No. 3 Results".center(130,"="))
    print((player_name + " Total goals "+ str(goals)).center(100))
    print((player_name + " Total penaltys "+ str(penalty)).center(100))
    print((player_name + " Total autogoals "+ str(own_goal)).center(100))

    if size > 6:
        print("Resultrs struct has more than 6 records...")
    else:
        print("Resultrs struct has less than 6 records...")
    print(tb.tabulate(dtos["elements"], headers = "keys" , tablefmt='grid'))



def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6


    print("Req No. 6 Input".center(130,"="))

    tournament_name =  input("Tournament name: ")
    n = int(input("Top N: "))
    star_date =  input("Start date: ")
    end_date =  input("End date: ")
    u ,n_teams, n_partidos,n_paises,n_ciudades, size_i =  controller.req_6(control,star_date, end_date, tournament_name,n)

    print("Req No. 6 Results".center(130,"="))
    print((tournament_name + " Total teams "+ str(n_teams)).center(100))
    print((tournament_name + " Total matches "+ str(n_partidos)).center(100))
    print((tournament_name + " Total countries "+ str(n_paises)).center(100))
    print((tournament_name + " Total cities "+ str(n_ciudades)).center(100))
    print((tournament_name + " Total teams "+ str(n_teams)).center(100))
    if size_i > 6:
        print("Resultrs struct has more than 6 records...")
    else:
        print("Resultrs struct has less than 6 records...")
    print(tb.tabulate(u["elements"], headers = "keys" , tablefmt='grid'))


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
        

    # TODO: Imprimir el resultado del requerimiento 7
    print("Req No. 7 Input".center(130,"="))
    tamanio =  int(input("Top N: "))
    date_i =  input("Start date: ")
    date_f =  input("End date: ")
    dtos, players, matches, goals, penalties, own_goals, size = controller.req_7(control, tamanio,  date_i, date_f)
    print("Req No. 7 Results".center(130,"="))
    print(("Official tournaments total players: "+ str(players)).center(100))
    print(("Official tournaments total matches: "+ str(matches)).center(100))
    print(("Official tournaments total goals: "+ str(goals)).center(100))
    print(("Official tournaments total penalties: "+ str(penalties)).center(100))
    print(("Official tournaments total own goals: "+ str(own_goals)).center(100))
    
    if size > 6:
        print("Resultrs struct has more than 6 records...")
    else:
        print("Resultrs struct has less than 6 records...")
    print(tb.tabulate(dtos["elements"], headers = "keys" , tablefmt='grid'))


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    x , y = controller.req_8(control)
    print(tb.tabulate(x["elements"], headers = "keys", tablefmt='grid'))




    

# Se crea el controlador asociado a la vista
control = new_controller()
# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("".center(130,"-"))
            print("Cargando información de los archivos ....".center(130))
            print("".center(130,"-"))
            results , goalscorers , shootouts = load_data(control)
            print(print_carga(control))
            

        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)


        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
