import numpy as np
t=0
w=np.array([-1,1])
eta=0.05
dt=0.025
T=[]
D=[]
Y=[]
for i in range(1000):
    x=np.sin(np.sin(10*np.square(t)))
    d=2*x+0.8
    y=w.dot(np.array([-1,x]))
    e=d-y
    w=w+eta*e*np.array([-1,x])
    T.append(t)
    D.append(d)
    Y.append(y)
    t=t+dt

print(w)
import matplotlib.pyplot as plt
plt.figure(1)
plt.plot(T,D,'o')
plt.xlabel('Time')
plt.ylabel('System output')
plt.figure(2)
plt.plot(T,D,'o')
plt.plot(T,Y,'r-')
plt.xlabel('Time')
plt.ylabel('Adaline output')
plt.show()