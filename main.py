from glob import glob
from re import X
import matplotlib.pyplot as plt
import numpy as np

#parametros
Vcc = 12
p = 10000
t = np.linspace(0,60,p)
R = 220
C = 10
global b
b = False

global Vc
Vc = []
for i in t:
    x = Vcc * (1 - np.exp(-i/R*C))
    
    alvoV = 3
    if x > alvoV and b == False:
        print("Vc: "+str(x) +" tempo: " + str(i)) 
        b = True
    #como achar o par de valores mais próximo a um
    #estante de tempo desejado 
    alvotempo = -1
    if (alvotempo - i) <= (61/p) and (alvotempo - i) > 0: 
        print("Vc: "+str(x) +" tempo: " + str(i))
    Vc.append(x)


fig, ax = plt.subplots()

ax.set_xlim([0,np.amax(t)])
ax.set_xlabel("t (segundos)") # pôe uma label no eixo x

ax.set_ylabel("Vc (tensão no capacitor)")
ax.set_ylim([0,13])

ax.set_yticks(np.arange(0,13,1))

ax.grid(True)

ax.plot(t,Vc)
plt.show()
    
        
