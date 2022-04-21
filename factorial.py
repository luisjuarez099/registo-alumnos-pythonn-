def factorial():
    contador=int(input("Introduce un numero para su factorial: "))
    i=1
    num=1
    while i<=contador:
        num=i*num
        i+=1
    print(f"El factorial de {contador} es: {num}")

if __name__=='__main__':
    factorial()
