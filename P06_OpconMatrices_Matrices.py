#Suma y resta
#Requieren que el orden de las matrices sea el mismo
#Pueden ser cuadradas o rectangulares
import numpy as np
A = np.array ([1,2],[2,3])
B = np.array ([3,4],[5,2])

print(A)
print(B)

C=A+B
print("Resultado de la suma de A+B")
print(C)

C= A-B
print("Resultado de la resta de A-B")
print(C)

#no es la multiplicacion matricial mucho ojo cuate

C= A*B
print("Resultado de la multiplicacion de A*B")
print(C)

C = A.dot(B)
print ("Multiplicacion matricial de A*B: ")
print (C)