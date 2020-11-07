
# Write your code here :-)
# Código anterior. Realice aquí las mejoras

#funcion que me devuelve true si divisieble por cualquiera de los numero y falso si no lo es
def divisible(numero):
    if numero%2==0 or numero%3==0 or numero%5==0:
       return True
    else:
        return False

##Declaro e inicializo la lista
lista=list(range(1,101))
#for i in range(1,101):
 #   lista.append(i)

#recorro la lista y llamo a la funcion divisible por cada numero
contador=0
for numero in lista:

    if divisible(numero):
        if contador==10:
            print("\n")
            contador=0
        else:
            print (numero,"*",end=' ',sep='')
    else:
        if contador==10:
            print("\n")
            contador=0
        else:
            print (numero,end=' ',sep='')
            #print(contador)
    contador=contador+1
