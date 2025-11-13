import numpy as np
print ("A en forma de lista de python")
A=[["alejandro",4,4,5],["Javier", 5, 6]]
print(A)
print("A en forma matricial")
A= numpy.array(A)
print(A)

orden = A.shape #no devuelve un string devuelve una tupa aka un tipo de dato que no se puede cambiar por eso tiene que ser casteado
print("Orden;" + str(orden))