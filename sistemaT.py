import os
import csv
import pandas as pd
os.system("cls" if os.name == "nt" else 'clear')

info = []
def Agregar():
    tarea=[]
    tarea.append(input("Ingresa tu nueva tarea: "))
    tarea.append(input("Ingresa la prioridad de la tarea (1. Alta, 2. Media, 3. Baja): "))
    return tarea

def VerTareasP():

    tareas_alta = [tarea for tarea in info if tarea[1] == "1"]
    tareas_media = [tarea for tarea in info if tarea[1] == "2"]
    tareas_baja = [tarea for tarea in info if tarea[1] == "3"]

    # Mostrar tareas por prioridad alta
    for tarea in tareas_alta:
        print("Tarea principal: ", tarea[0])
        print("Prioridad: Alta")
        print("--------------------------------")

    # Mostrar tareas por prioridad media
    for tarea in tareas_media:
        print("Tarea secundaria: ", tarea[0])
        print("Prioridad: Media")
        print("--------------------------------")

    # Mostrar tareas por prioridad baja
    for tarea in tareas_baja:
        print("Tarea no urgente: ", tarea[0])
        print("Prioridad: Baja")
        print("--------------------------------")
with open('tareas.csv', newline='') as f:
    reader = csv.reader(f)
    for lin in reader:
        t=[]
        t.append(lin[1])
        t.append(lin[2])
        info.append(t)

def Eliminar():
    # Leer el archivo CSV y cargar los datos en un DataFrame
    df = pd.read_csv('tareas.csv')

    tarea_num = input("Ingrese el número de tarea que desea eliminar: ")
    tarea_idx = int(tarea_num) - 1  # Convertir el número de tarea a un índice válido

    if 0 <= tarea_idx < len(df):
        # Eliminar la tarea del DataFrame
        df = df.drop(tarea_idx)

        # Guardar el DataFrame actualizado en el archivo CSV sin incluir el índice
        df.to_csv('tareas.csv', index=False)
        print("Tarea eliminada exitosamente.")
    else:
        print("Número de tarea no válido. Intente nuevamente.")

def Modificar():
    tarea=input("Ingrese el número de tarea que desea modificar: ")
    if tarea=="1":
        info[0]=Agregar()
        df= pd.DataFrame(info, columns=['Tarea principal', 'Prioridad'])
        df.to_csv('tareas.csv')

def menu():
    print("1. Agregar")
    print("2. Modificar")
    print("3. Ver tareas pendientes")
    print("4. Salir")
    print("5. Eliminar alguna tarea")
    print(chr(22), chr(22), chr(22), chr(22), chr(22), chr(22), chr(22), chr(22), chr(22), chr(22), chr(22), chr(22), chr(22), chr(22), chr(22), chr(22))
    opt=input("Ingrese su opción: ")
    if opt=="1":
        info.append(Agregar())
        input("Se agregó una tarea correctamente")
        print(chr(3), chr(3), chr(3), chr(3), chr(3), chr(3), chr(3), chr(3), chr(3), chr(3), chr(3), chr(3), chr(3), chr(3), chr(3), chr(3), chr(3))
        menu()
        print("--------------------------------")
    if opt=="2":
        Modificar()
        input("Se ha modificado correctamente")
        menu()
    if opt=="3":
        VerTareasP()
        input("Estas son las tareas pedientes")
        print(chr(3), chr(3), chr(3), chr(3), chr(3), chr(3), chr(3), chr(3), chr(3), chr(3), chr(3), chr(3), chr(3), chr(3), chr(3), chr(3), chr(3))
        menu()
        print("--------------------------------")
    if opt=="4":
        df= pd.DataFrame(info, columns=['Tarea', 'Prioridad'])
        df.to_csv('tareas.csv')
    if opt=="5":
        Eliminar()
        input("Se eliminó correctamente la tarea")
        menu()
menu()
