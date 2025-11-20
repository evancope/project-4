import numpy as np
import parameters as P


def vanderpol1(t, y):
    y1dot = y[1]
    y2dot = (P.u[0] * (1 - y[0] ** 2) * y[1]) - y[0]
    return y1dot, y2dot
def vanderpol500(t, y):
    y1dot = y[1]
    y2dot = (P.u[1] * (1 - y[0] ** 2) * y[1]) - y[0]
    return y1dot, y2dot
def belousov(t, y):
    y1dot = 77.27 * (y[1] - y[0] * y[1] + y[0] - 8.375 * (10 ** (-6)) * (y[0] **2))
    y2dot = (-y[1] - y[0] * y[1] + y[2]) / 77.27
    y3dot = 0.161 * (y[0] - y[2])
    return y1dot, y2dot, y3dot
def houwen(t, y):
    y1dot = 0.2 * (y[1] - y[0])
    y2dot = 10 * y[0] - (60 - 0.125 * t) * y[1] + 0.125 * t
    return y1dot, y2dot
def dp(t, y):
    C = np.cos(y[0] - y[2])
    S = np.sin(y[0] -y[2])
    y1dot = y[1]
    y2dot = (- C * S * (y[1] ** 2) - S* (y[3] **2) - 2 * (P.w ** 2) \
             * np.sin(y[0]) + C * (P.w ** 2) * np.sin(y[2])) / (2 - (C ** 2))
    y3dot = y[3]
    y4dot = (2 * (y[1] ** 2) * S + S * C * (y[3] ** 2) + 2 * C * (P.w ** 2)\
              * np.sin(y[0]) - 2 * (P.w ** 2)* np.sin(y[2])) / (2 - (C ** 2))
    return y1dot, y2dot, y3dot, y4dot

def cartesian(theta, phi):
    N = len(theta)
    x = []
    y = []
    for i in range(N):
        y.append(- P.l * (np.cos(theta[i]) + np.cos(phi[i])))
        x.append(P.l * (np.sin(theta[i]) + np.sin(phi[i])))
    return x, y

def append_to_file(my_list, filename):
    with open(filename, 'a') as file:
        for item in my_list:
            file.write(f"{item}\n")