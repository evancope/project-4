u = [1, 500]
g = 9.81
l = 1
w = g / l

y0_vanderpole = [2, 0]
y0_belousov = [4, 1.1, 4]
y0_houwen = [0, 0]
y0_ddp = [0 ,-1, 0, 1]

tspan_vanderpole = [[0, 200], [0, 1000]]
tspan_belousov = [0, 350]
tspan_houwen = [0, 400]
tspan_ddp = [0, 40]

tolerance_vanderpole = 10 ** (-10)
tolerance_belousov = 10 ** (-6)
tolerance_houwen = 10 ** (-7)
tolerance_ddp = 10 ** (-6)

