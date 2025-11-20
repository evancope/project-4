import scipy.integrate as ode
from functions import dp, cartesian
import parameters as P
import matplotlib.pyplot as plt
import time
import numpy as np

t_i = P.tspan_dp[0]
t_f = P.tspan_dp[1]
y0 = P.y0_dp


solution45 = ode.RK45(dp,t_i,y0,t_f,atol = P.tolerance_dp)
solution113 = ode.LSODA(dp,t_i,y0,t_f,atol = P.tolerance_dp)
solution15s = ode.BDF(dp,t_i,y0,t_f,atol = P.tolerance_dp)


# Collect data for RK45
t45 = [t_i]
y1_values45 = [y0[0]]
y2_values45 = [y0[1]]
y3_values45 = [y0[2]]
y4_values45 = [y0[3]]
#Get solution for RK45
start45 = time.process_time()
while solution45.status == 'running':
    solution45.step()
    t45.append(solution45.t)
    y1_values45.append(solution45.y[0])
    y2_values45.append(solution45.y[1])
    y3_values45.append(solution45.y[2])
    y4_values45.append(solution45.y[3])
end45 = time.process_time()
print(f"CPU time for RK45: {end45 - start45} seconds")
#Plot data for RK45
plt.figure()
plt.plot(t45, y1_values45,\
          label = 'y1', color = 'red')
plt.plot(t45, y2_values45,\
          label = 'y2', color = 'green')
plt.plot(t45, y3_values45,\
          label = 'y3', color = 'blue')
plt.plot(t45, y4_values45,\
          label = 'y4', color = 'black')
plt.title('RK45 solution to double pendulum')
plt.legend()
plt.grid()
plt.show()


CartesianValues45 = cartesian(y1_values45, y2_values45)
plt.figure()
plt.plot(CartesianValues45[0],CartesianValues45[1],\
          label = 'x,y', color = 'blue')
plt.title('RK45 cartesian motion of double pendulum')
plt.legend()
plt.grid()
plt.show()