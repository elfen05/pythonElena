import json
import os
paises={}


def leePais():
  pais=input('Nombre del país: ')
  lider=input('Presidente: ')
  capital=input('Capital: ')
  return pais, {"lider": lider, "capital": capital}

def leeArchivo():
    with open("paises.json","r") as file:
        return(json.load(file))

def anadirPais(): # con archivos
  #vamos a sobreescribir el archivo
  # Research. How write at the end?
    pais,datos=leePais()
    paises[pais]=datos
    print("Listo!!")
    print("\t")
    return

def escribePais():
    #print(paises)
    with open("paises.json","w") as file:
        file.write(json.dumps(paises))
        file.close()

def verPais():
    print("los paises que tengo son: ")
    print("\t")
    paises=cargaArchivo()
    #print(paises)
    listaPaises=paises.keys()
    for pais in listaPaises:
       print("Pais: " , pais)
       datosPais=paises[pais].keys() # paises variable global en la key "pais". Trae los key de presidente y capital
       for dato in datosPais:
           print("\t ",dato,": ",paises[pais][dato])
    return

def cargaArchivo():
    #with open("paises.json","r") as file:
    #need to import libreria
        if os.stat("paises.json").st_size == 0:
            print("el archivo esta vacio")
            return {} #??

        else:
            return leeArchivo()



def menu():
    print("\t         Bienvenido ")
    print("\t Digite una opcion del menu:")
    print("\t 1. Añadir un pais a lista")
    print("\t 2. Mostrar la lista de paises")
    print("\t 3. Borrar un pais")
    print("\t 4. Salir")
    opcion=int(input("opcion: "))
    print("\t")
    if (opcion <= 4 and opcion >= 1 ):
        #print("opcion valida!", opcion)
        #menu()
        return opcion
    else :
        print("Por favor introduzca una opcion valida", opcion)
        print("\t")
        menu()

while True:
    #menu()
    print("\t")
    option=menu()

    if (option==1):
        paises=cargaArchivo()
        anadirPais()
        escribePais()# solo al final o salir del programa
        #menu()
    elif(option==2):
        paises=cargaArchivo()
        verPais()
        #menu()
    elif(option==3):
        print("carga archivo")
        cargaArchivo()

        #menu()
    elif(option==4):
        print("4 por definir")
        #menu()

    #break
    #anadirPais()
    #verPais()