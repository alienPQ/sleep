import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define the non-autonomous ODE system
def nonautonomous_ode(t, y, a, b, c, d):
    dydt = [a*y[0] + b*y[1] + np.sin(c*t),
            c*y[0] - d*y[1] + np.cos(d*t)]
    return dydt

# Set parameters
a = 1.0
b = -2.0
c = 0.5
d = 0.5

# Initial conditions
y0 = [1.0, 0.5]

# Time span
t_span = [0, 10]

# Time points where the solution will be computed
t_eval = np.linspace(t_span[0], t_span[1], 1000)

# Solve the non-autonomous ODE system
solution = solve_ivp(nonautonomous_ode, t_span, y0, t_eval=t_eval, args=(a, b, c, d))

# Plot the solution
plt.figure(figsize=(8, 6))
plt.plot(solution.t, solution.y[0], label='y1(t)')
plt.plot(solution.t, solution.y[1], label='y2(t)')
plt.xlabel('Time (t)')
plt.ylabel('Solution')
plt.title('Non-autonomous ODE System Solution')
plt.legend()
plt.grid(True)
plt.show()
