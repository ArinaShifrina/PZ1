import os
import numpy as np
import matplotlib.pyplot as plt
import math

Xs = -10
Xf = 10
dX = 0.01
A = 0

X = [i*dX+Xs for i in range(int((Xf-Xs)/dX))]
Y = []

for i in range(len(X)):
	Temp = X[i]
	Y.append(0.5 + (math.sin(Temp*Temp - A*A)**2 - 0.5)/abs(1 + 0.001*(Temp*Temp + A*A)))

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'results')
if os.path.exists(filename)==False:
    os.mkdir(filename)
filename = os.path.join(filename, 'results.json')

with open(filename,'w') as f:
        f.write('{\n\t')
        for i in range(len(X)):
            Temp = str(X[i]) + ', '
        Temp = Temp[:-2]
        f.write('"x": [' + Temp + '],\n')
        for i in range(len(Y)):
            Temp = str(Y[i]) + ', '
        Temp = Temp[:-2]
        f.write('\t"y": [' + Temp + ']\n}')

plt.plot(X,Y)
plt.show()
