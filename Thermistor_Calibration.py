import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit  

r = 10000
v0_1 = np.array([2.30, 2.15, 1.47, 1.44, 1.20, 1.07, 0.89, 0.78, 0.67, 0.64, 0.52]) ##Sensor 7
v0_2 = np.array([2.076, 2.026, 1.66, 1.49, 1.32, 1.02, 0.83, 0.67, 0.59, 0.56, 0.58]) ##Sensor 8
v0_3 = np.array([2.56, 2.18, 2.04, 1.96, 1.42, 1.23, 1.04, 0.91, 0.79, 0.72, 0.57]) ##Sensor 6
v0_4 = np.array([2.90, 2.36, 1.95, 1.71, 1.50, 1.31, 1.14, 0.96, 0.84, 0.74, 0.65]) ##Sensor 5
ve = 5

def lab(r,v0,ve):
    deltav = ve - v0
    rg = r*(v0)/(deltav)
    print(rg)
    T = np.array([25 + 5*i for i in range(11)])
    def mapping1(values_x, a, b):  
        return a*(np.e)**(b/values_x)
    args, covar = curve_fit(mapping1, T, rg) 
    a = args[0]
    b = args[1]
    #a = 856.0945777984579
    #b = 62.67692869526935
    rg_fit = a*(np.e)**(b/T) 
    err_rg  = ((rg_fit - rg)/rg_fit)
    dV0_dT = (r*b*ve)/(T**2 * rg * ((r/rg)+1))
    plt.plot(T,rg) #Rg vs Temp plot 
    plt.plot(T, rg_fit) #Rg aprrox fit
    plt.show()
    plt.plot(T, err_rg)
    plt.show()
    print(a) #K
    print(b) #bita
    plt.plot(T, dV0_dT)  #Sesitivity plot
    print(dV0_dT) # dV/dT array  
    plt.show()
lab(r,v0_4,ve)
a1, b1 = 737.7129102639709, 63.187207170668096
a2, b2 = 863.7049102787149, 55.9441088912233
a3, b3 =  1027.868995587942, 59.758502846826765
a4, b4 = 795.0914950632035, 71.81789587235927
a = (a1+a2+a3+a4)/4
b = (b1+b2+b3+b4)/4