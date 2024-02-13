import os
import pandas as pd
os.system("cls" if os.name == "nt" else 'clear')

info = []
def Agregar():
    tarea=[]
    tarea.append(input("Ingresa tu nueva tarea: "))
    tarea.append(input("Ingresa la prioridad de la tarea (1. Alta, 2. Media, 3. Baja): "))
    info.append(tarea)
    return tarea

dtmp=pd.read_csv("C:/ed2024/tareas.csv")
tmp=dtmp.values.tolist()
for lin in tmp:
    t=[]
    t.append(lin[0])
    t.append(lin[1])
    info.append(t)
print("Datos cargados del CSV:", info)

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
chc=0
miarchivo=open('tareas.csv', 'r')
lectura=miarchivo.readline()
#tmp=dtmp.values.tolist()


def Modificar():
    tarea=input("Ingrese el número de tarea que desea modificar: ")
    if tarea=="1":
        info[0]=Agregar()
        df= pd.DataFrame(info, columns=['Tarea principal', 'Prioridad'])
        df.to_csv("C:/Users/anaka/OneDrive - Universidad de Guadalajara/tareas.csv")
    if tarea=="2":
        info[1]=Agregar()
        df= pd.DataFrame(info, columns=['Tarea principal', 'Prioridad'])
        df.to_csv("C:/Users/anaka/OneDrive - Universidad de Guadalajara/tareas.csv")
    if tarea=="3":
        info[2]=Agregar()
        df= pd.DataFrame(info, columns=['Tarea principal', 'Prioridad'])
        df.to_csv("C:/Users/anaka/OneDrive - Universidad de Guadalajara/tareas.csv")
    if tarea=="4":
        info[3]=Agregar()
        df= pd.DataFrame(info, columns=['Tarea principal', 'Prioridad'])
        df.to_csv("C:/Users/anaka/OneDrive - Universidad de Guadalajara/tareas.csv")
    if tarea=="5":
        info[4]=Agregar()
        df= pd.DataFrame(info, columns=['Tarea principal', 'Prioridad'])
        df.to_csv("C:/Users/anaka/OneDrive - Universidad de Guadalajara/tareas.csv")

def menu():
    print("1. Agregar")
    print("2. Modificar")
    print("3. Ver tareas pendientes")
    print("4. Ver tareas hechas")
    print("5. Salir")
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
        VerTareasH()
    if opt=="5":
        df= pd.DataFrame(info, columns=['Tarea principal', 'Prioridad'])
        df.to_csv("C:/ed2024/tareas.csv")
menu()
