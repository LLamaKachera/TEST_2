##Realizando ejercicios para estar en forma - n1 ..DUCKcity..
'''
Considere como ejemplo el número primo 3797. Este número puede descomponerse en varias
partes: (3, 797)(37, 97)(379, 7) que cuando se concatenan, da el número original. La caracteristica
que tienen estas descomposiciones, es que cada una de ellas es un número primo.
En el ejemplo, los números: 3, 37, 379, 797, 97, 7 son todos números primos.
El número 9982373. sólo puede descomponerse como sigue:(99823, 73)(998237, 3)
'''
##entrada
'''
La primera línea indica el número de casos de prueba. Luego, por cada caso de prueba viene un
número primo, cada uno en una nueva línea.
'''
##IN
'''
2
3797
9982373
'''
##OUT
'''
(3, 797) (37, 97) (379, 7)
(99823, 73) (998237, 3)
'''
##################################################
def f_separate(x):
    str_var_a = str(x)
    print(str_var_a[1])
    
    
n = int(input())
for _ in range (n):
    t = int(input())
    f_separate(t)