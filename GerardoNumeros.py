def numerosdivisibles(lista):
    for n in range(0,len(lista)):
        if lista[n]%2==0 or lista[n]%3==0 or lista[n]%5==0:
            resultado = print("$",lista[n], "\t", end=' ')
            n=n+1
        else:
            resultado = print(lista[n], "\t", end=' ')
            n=n+1
    return resultado



numeros = list(range(1, 101))
#valores = numerosdivisibles(numeros)
#print (valores)
#Solo llamando a la funcion para imprimir lo que tiene sin igualarla a una variable e imprimr la variable
numerosdivisibles(numeros)