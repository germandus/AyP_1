#UNIDAD 5: Más sobre ciclos


#ej 5.1 - Promedio de notas
'''
Escribir un programa que permita al usuario ingresar un conjunto de notas, preguntando a cada 
paso si desea ingresar más notas, e imprimiendo el promedio correspondiente.
'''
'''
def ingreso_notas() -> list:
    """
    Pide notas
    """
    cortar = False
    notas = list()

    while not cortar:
        n = int(  input('Ingrese una nota: '))
        notas.append(n)
        opc = ( input('Desea ingresar mas notas? (s/n): ') )
        if opc == 'n':
            cortar = True 
    
    return notas


def muestra_promedio_notas(notas) -> None:
    """
    muestra promedio
    """
    sum = 0
    for nota in notas:
        sum += nota
    print('El promedio es: ', sum/( len(notas) ) ) 

def main():
    """
    Lee notas (de a una) del usuario, preguntando en cada paso si se desea continuar. 
    Al finalizar, se imprime el promedio de las mismas.
    """
    notas = ingreso_notas()
    muestra_promedio_notas(notas)

main()
'''

#ej 5.2 - Descomposicion en factores primos de
'''Escribir una función que reciba un número entero k e imprima su descomposición en factores 
primos.'''
#version normal
'''
def descomposicion_factores_primos(k):
    """
    DOC: Completar
    """
    for i in range(2,k + 1):
        while k % i == 0:
            k /= i
            print(i)

k =  int ( input('n: ') )
descomposicion_factores_primos(k)
'''
#version de un estup***
'''
def es_primo(n) -> bool:
    """
    dice si es primo o no
    """
    es_primo = True
    divisor = n-1
    while divisor >1 and es_primo:    
        
        if n % divisor == 0:
            es_primo = False
        
        divisor -=1
    
    return es_primo
"""
import math
def es_primo(n):
    if n <= 0:
        return False
    cant_divisores = 0
    encontro_divisores = False
    limite=math.sqrt(n)
    i = 2
    while (i <= limite and not encontro_divisores):
        if n % i == 0:
            cant_divisores+=1
            encontro_divisores = True
        i+=1
    if cant_divisores==0 and n>1:
        return True
    return False 
"""

def descomposicion_en_factores_primos(tupla: tuple) -> None:
    """
    muestra factores primos de k
    """ 
    lista_primos = tupla [0] 
    k = tupla[1]

    i=k
    if k == 1:
        lista_primos = lista_primos[::-1] 
        for primo in lista_primos:
            print(primo)
        return lista_primos,k
    
    while k >1:
        if k % i == 0:     
            if es_primo(i):
                lista_primos.append(i)
                lista_primos, k = descomposicion_en_factores_primos( (lista_primos,k//i) )
        i -=1
    return lista_primos,k


def descomposicion_factores_primos(k: int):
    """
    """
    k = k
    l = list()
    tupla = (l,k)
    descomposicion_en_factores_primos(tupla)

k = int (input('n: '))
descomposicion_factores_primos(k)

# def main():
#     l = list()
#     n = int( input('n: ')) 
#     descomposicion_factores_primos( (l,n) )

# main()
'''
