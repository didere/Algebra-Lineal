X=[
[47,29,	28,	69,	56,]
[82,69,	11,	3,	45,]
[83,35,	52,	96,	21,]
[27,74,	50,	43,	8,]
[17,31,	32,	59,	53,]
[10,35,	30,	49,	83,]
[49,70,	26,	50,	88,]
[53,31,	51,	12,	29,]
[83,74,	40,	29,	83,]
[45,17,	47,	90,	82,]
[12,62,	78,	6,	21,]
[67,1,	81,	70,	39,]
[70,3,	36,	83,	3,]
[0,	44,	11,	40,	48,]
[54,29,	19,	59,	74,]
[1,	54,	0,	3,	78,]
[68,18,	64,	62,	31,]
[50,46,	96,	87,	63,]
[87,91,	73,	35,	98,]
[60,49,	29,	87,	9,]
]

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