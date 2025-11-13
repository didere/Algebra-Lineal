x = []
#no vectores son listas vector: un conjunto de datos del mismo tipo que se encuentran relacionados
# listas: conjunto de datos que no necesariamente son relacionados
y = []

#x -10 a 10
X= [v for v in range (-10, 11, 1)]
print(X)

#y = x a la 2da potencia
y = [x**2 for x in X]
print (y)

from matplotlib import pyplot as plt
plt.plot(X,y)
plt.grid(True)
plt.show()