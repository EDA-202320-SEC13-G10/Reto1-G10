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




def print_req_1(control,pais,tipolocal,n):
    l1,l2=controller.req_1(control,pais,tipolocal,n)
    print(tb.tabulate(l1["elements"], headers = "keys" , tablefmt='grid'))
    print(l2)
    
    
def print_req_2(control , nombre, n):
    """
        Función que imprime la solución del Requerimiento 2 
        en consola
    """
    l1,l2=controller.req_2(control,nombre,n)
    print(tb.tabulate(l1["elements"], headers = "keys", tablefmt='grid'))
    print(l2)
    


def print_req_3(control,date_i, date_f , team):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    dtos, home_matchs, away_matchs, total, tiempo = controller.req_3(control,date_i, date_f , team)
    print(tb.tabulate(dtos["elements"], headers = "keys", tablefmt='grid'))
    print(home_matchs)
    print(away_matchs)
    print(total)
    print(tiempo)




def print_req_4(control, date_i, date_f, tournament):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 41
    dtos, matches, countries, cities, shootouts = controller.req_4(control, date_i, date_f, tournament)
    print(tb.tabulate(dtos["elements"], headers = "keys", tablefmt="grid"))
    print(matches)
    print(countries)
    print(cities)
    print(shootouts)


def print_req_5(control, date_i, date_f , nombre):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    dtos, penalty, own_goal =  controller.req_5(control, date_i, date_f , nombre)
    print(tb.tabulate(dtos["elements"], headers = "keys", tablefmt='grid'))
    print(penalty)
    print(own_goal)


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control, tamanio,  date_i, date_f):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    dtos, players, matches, goals, penalties, own_goals = controller.req_7(control, tamanio,  date_i, date_f)
    print(tb.tabulate(dtos["elements"], headers = "keys", tablefmt='grid'))
    print(players)
    print(matches)
    print(goals)
    print(penalties)
    print(own_goals)


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass



    

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
            print_carga(control)

        elif int(inputs) == 2:
            print_req_1(control,"Italy","home",15)

        elif int(inputs) == 3:
            print_req_2(control, "Rodolph Austin" , 7)

        elif int(inputs) == 4:
            print_req_3(control,"1939-01-01","1980-12-31","Germany")

        elif int(inputs) == 5:
            print_req_4(control, "1955-06-01", "2022-06-30", "Copa América")

        elif int(inputs) == 6:
            print_req_5(control, "1999-03-25", "2021-11-23", "Ali Daei")

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control, 17, "2002-01-25", "2021-11-23")

        elif int(inputs) == 9:
            print_req_8(control)


        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
