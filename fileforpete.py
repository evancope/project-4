import scipy.integrate as ode
from functions import belousov, append_to_file
import parameters as P
import matplotlib.pyplot as plt
import time

t_i = P.tspan_belousov[0]
t_f = P.tspan_belousov[1]
y0 = P.y0_belousov


solution45 = ode.RK45(belousov,t_i,y0,t_f,atol = P.tolerance_belousov)

# Collect data for RK45
t45 = [t_i]
y1_values45 = [y0[0]]
y2_values45 = [y0[1]]
y3_values45 = [y0[2]]
#Get solution for RK45
start45 = time.process_time()

while solution45.status == 'running':
    solution45.step()
    t45.append(solution45.t)
    y1_values45.append(solution45.y[0])
    y2_values45.append(solution45.y[1])
    y3_values45.append(solution45.y[2])

end45 = time.process_time()

append_to_file(t45, 't45.txt')
append_to_file(y1_values45, 'y1_45.txt')
append_to_file(y1_values45, 'y2_45.txt')
append_to_file(y1_values45, 'y3_45.txt')


print(f"CPU time for RK45: {end45 - start45} seconds")


