def divisible():
    for i in range (0,101):
        if i%2==0 or i%3==0 or i%5==0:
            resultado=print (i,"/t Numero divisible")
            i+=1
        else:
            resultado= print (i,"/t Numero primo")
            i+=1
   # return resultado

divisible()