'''
             Programa elaborado por Daniela Carrillo C.I 28.101.501
             Fecha:12-02-2024
             El siguiente programa resta dos números reales e imprime el resultado en pantalla
'''

dato1= float (input("Ingrese el primer valor:"))
dato2= float(input("Ingrese el segundo valor:"))

resultadoResta=dato1 - dato2
#agregamos condicional en caso que la resta sea <0

if resultadoResta < 0: 

    print("\033[;31m"+"El resultado es negativo:"+'\033[0;m',resultadoResta)
else:

    print("El resultado de la resta es=",resultadoResta)