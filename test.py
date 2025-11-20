import scipy as sc
import scipy.integrate as si
import numpy as np

def f(t, x):
    k = 6
    m = 2
    xdoubledot = - k * x / m
    