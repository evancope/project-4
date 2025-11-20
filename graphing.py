import scipy as sc
import scipy.integrate as si
import matplotlib.pyplot as plt
from functions import vanderpol, belousov, houwen, ddp
import parameters as P
import numpy as np
N = 10000
t = np.linspace(P.tspan_belousov[0],P.tspan_belousov[1],N)
S1 = [0]
for i in range(0,N):
    S = si.RK45(belousov,t[0] , P.y0_belousov,\
            t[i], atol=P.tolerance_belousov, vectorized=True)
    S1.append(S)

plt.figure()
plt.plot(t, S1,\
          label = 'belousov solution', color = 'r')
plt.title('rk45 solution to belousov function')
plt.legend()
plt.grid()
plt.show()
