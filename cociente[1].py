'''
             Programa elaborado por Daniela Carrillo C.I 28.101.501
             Fecha:12-02-2024
             El siguiente programa divide dos números reales e imprime el resultado en pantalla
'''

numerador= float (input("Ingrese el primer valor:"))
denominador= float(input("Ingrese el segundo valor:"))


#Agregar el condicional si se divide entre 0 es indeterminación 

if denominador!=0:
    cociente=numerador / denominador
    print("\033[34m"+"El resultado es:"+'\033[0;m',cociente)

else:
    print("\033[4;31m"+"El resultado es una indeterminación ya que está intentando dividir entre 0"+'\033[0;m')
