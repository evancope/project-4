import scipy.integrate as ode
from functions import vanderpol1
import parameters as P
import matplotlib.pyplot as plt
import time

t_i = P.tspan_vanderpole[0][0]
t_f = P.tspan_vanderpole[0][1]
y0 = P.y0_vanderpole


solution45 = ode.RK45(vanderpol1,t_i,y0,t_f,atol = P.tolerance_vanderpole)
solution113 = ode.LSODA(vanderpol1,t_i,y0,t_f,atol = P.tolerance_vanderpole)
solution15s = ode.BDF(vanderpol1,t_i,y0,t_f,atol = P.tolerance_vanderpole)


# Collect data for RK45
t45 = [t_i]
y1_values45 = [y0[0]]
y2_values45 = [y0[1]]
#Get solution for RK45
start45 = time.process_time()
while solution45.status == 'running':
    solution45.step()
    t45.append(solution45.t)
    y1_values45.append(solution45.y[0])
    y2_values45.append(solution45.y[1])
end45 = time.process_time()
print(f"CPU time for RK45: {end45 - start45} seconds")
#Plot data for RK45
plt.figure()
plt.plot(t45, y1_values45,\
          label = 'y1', color = 'red')
plt.plot(t45, y2_values45,\
          label = 'y2', color = 'green')
plt.title('RK45 phase plot vanderpol function u = 1')
plt.legend()
plt.grid()
plt.show()

plt.figure()
plt.plot(y1_values45,y2_values45,\
          label = '', color = 'red')

plt.title('RK45 phase plot for vanderpol function u = 1')
plt.legend()
plt.grid()
plt.show()

# Collect data for ABM
t113 = [t_i]
y1_values113 = [y0[0]]
y2_values113 = [y0[1]]
#Get solution for ABM
start113 = time.process_time()
while solution113.status == 'running':
    solution113.step()
    t113.append(solution113.t)
    y1_values113.append(solution113.y[0])
    y2_values113.append(solution113.y[1])
end113 = time.process_time()
print(f"CPU time for ABM: {end113 - start113} seconds")
#Plot data for ABM
plt.figure()
plt.plot(t113, y1_values113,\
          label = 'y1', color = 'red')
plt.plot(t113, y2_values113,\
          label = 'y2', color = 'green')
plt.title('ODE113 solution to vanderpol function u = 1')
plt.legend()
plt.grid()
plt.show()

plt.figure()
plt.plot(y1_values113,y2_values113,\
          label = '', color = 'red')

plt.title('ODE113 phase plot for vanderpol function u = 1')
plt.legend()
plt.grid()
plt.show()

# Collect data for BDF
t15s = [t_i]
y1_values15s = [y0[0]]
y2_values15s = [y0[1]]
#Get solution for BDF
start15s = time.process_time()
while solution15s.status == 'running':
    solution15s.step()
    t15s.append(solution15s.t)
    y1_values15s.append(solution15s.y[0])
    y2_values15s.append(solution15s.y[1])
end15s = time.process_time()
print(f"CPU time for BDF: {end15s - start15s} seconds")
#Plot data for BDF
plt.figure()
plt.plot(t15s, y1_values15s,\
          label = 'y1', color = 'red')
plt.plot(t15s, y2_values15s,\
          label = 'y2', color = 'green')
plt.title('BDF solution to vanderpol function u = 1')
plt.legend()
plt.grid()
plt.show()

plt.figure()
plt.plot(y1_values15s,y2_values15s,\
          label = '', color = 'red')

plt.title('BDF phase plot for vanderpol function u = 1')
plt.legend()
plt.grid()
plt.show()