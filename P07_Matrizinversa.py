import numpy as np

A = np.array ([[1,2],[2,3]])
print (A)

Ainv = np.linalg.inv(A)
print (Ainv)

#comprobacion

print("Comprobacion: ")
C = A.dot(Ainv) #matriz a por la inversa de a
C2 = Ainv.dot (A) #inversa de a por a

print (C)
print(C2)