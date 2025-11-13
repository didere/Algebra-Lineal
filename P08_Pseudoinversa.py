X = ([
    [47,	82,	83,	27,	17,	10,	49,	53,	83,	45,	12,	67,	70,0,54,	1,	68,	50,	87,	60],
[29,    69,	35,	74,	31,	35,	70,	31,	74,	17,	62,	1,	3,	44,29,54,	18,	46,	91,	49],
[28,	11,	52,	50,	32,	30,	26,	51,	40,	47,	78,	81,	36,	11,19,0,	64,	96,	73,	29],
[69,	3,	96,	43,	59,	49,	50,	12,	29,	90,	6,	70,	83,	40,59,3,	62,	87,	35,	87],
[56,	45,	21,	8,	53,	83,	88,	29,	83,	82,	21,	39,	3,	48,74,78,	31,	63,	98,	9]
])

import numpy as np
X = np.array(X)
print (X)

Xinv = np.linalg.inv(X)

print (Xinv)

Xpseudoinv = np.linalg.pinv(X)
print(Xpseudoinv)

print("Comprobacion")

C=X.dot(Xpseudoinv)
C= np.round(C,2)
C2 = Xpseudoinv.dot(X)
C2 = np.round(C2,2)

print("X.dot(Pseudo)")
print(C)
print("X.dot(Pseudo)")
print(C2)