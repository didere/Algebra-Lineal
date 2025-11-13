#libreria = modulo en python

#dependiendo de la situacion se puede codificar de cero o usar una libreria las librerias pesan mas y son no personalizables

#Numpy operaciones matematicas
import numpy as np
mA = [3,4,5]

mB = [1,4,6]

print(mA)
print(mB)

mA = np.array(mA)
nB = np.array(mB)

print(mA)
print(nB)

print("C en forma de lista de python")
C=[[2,4][1,5]]
print(C)
print("C en forma matricial")
C= np.array(C)
print(C)

