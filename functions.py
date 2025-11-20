import numpy as np
import parameters as P


def vanderpol1(t, y):
    y1dot = y[1]
    y2dot = P.u[0] * (1 - y[0] ** 2) * y[1] - y[0]
    return y1dot, y2dot
def vanderpol500(t, y):
    y1dot = y[1]
    y2dot = P.u[1] * (1 - y[0] ** 2) * y[1] - y[0]
    return y1dot, y2dot
def belousov(t, y):
    y1dot = 77.27 * (y[1] - y[0] * y[1] + y[0] - 8.375 * (10 ** (-6)) * y[0] **2)
    y2dot = (-y[1] - y[0] * y[1] + y[2]) / 77.27
    y3dot = 0.161 * (y[0] - y[2])
    return y1dot, y2dot, y3dot
def houwen(t, y1, y2):
    y1dot = 0.2 * (y2 - y1)
    y2dot = 10 * y1 - (60 - 0.125 * t) * y2 + 0.125 * t
    return y1dot, y2dot
def ddp(t, y1, y2, y3, y4):
    C = np.cos(y1 - y3)
    S = np.sin(y1 -y3)
    y1dot = y2
    y2dot = (- C * S * (y2 ** 2) - S* (y4 **2) - 2 * (P.w ** 2) \
             * np.sin(y1) + C * (P.w ** 2) * np.sin(y3)) / (2 - (C ** 2))
    y3dot = y4
    y4dot = (2 * (y2 ** 2) * S + S * C * (y4 ** 2) + 2 * C * (P.w ** 2)\
              * np.sin(y1) - 2 * (P.w ** 2)* np.sin(y3)) / (2 - (C ** 2))
    return y1dot, y2dot, y3dot, y4dot
