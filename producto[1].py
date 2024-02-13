'''
             Programa elaborado por Daniela Carrillo C.I 28.101.501
             Fecha:12-02-2024
             El siguiente programa multiplica dos números reales e imprime el resultado en pantalla
'''

Valor1= float (input("Ingrese el primer valor:"))
Valor2= float(input("Ingrese el segundo valor:"))

producto=Valor1 * Valor2
 #condicional que todo numero multiplicado por 0=0
if Valor1==0 or Valor2==0:
   
    print("\033[;31m"+"Todo numero multiplicado por 0 da 0 por lo tanto el resultado es:"+'\033[0;m',producto)

else:
    print("El resultado de la multiplicación es:",producto)