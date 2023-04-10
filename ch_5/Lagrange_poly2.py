# Exercise 5.15
# *

import numpy as np
import matplotlib.pyplot as plt


def L_k(x, k, xp, yp):
    ans = 1
    for i in range(len(xp)):
        if i != k:
            ans *= (x - xp[i]) / (xp[k] - xp[i])
    return ans


def p_L(x, xp, yp):
    ans = 0
    for k in range(len(yp)):
        ans += yp[k] * L_k(x, k, xp, yp)
    return ans


def verify(xp, yp):
    status = 'Verified!'
    for k in range(len(xp)):
        if abs(p_L(xp[k], xp, yp) - yp[k]) > 1e-15:
            status = 'Error!'
            break
    print status


def verbose_verify(xp, yp):
    print '%10s %10s %10s %12s' % ('x', 'Exact', 'Approx', 'Difference')
    for k in range(len(xp)):
        x = xp[k]
        exact = yp[k]
        approx = p_L(xp[k], xp, yp)
        diff = abs(p_L(xp[k], xp, yp) - yp[k])
        print '%10f %10f %10f %12f' % (x, exact, approx, diff)


def graph(f, n, xmin, xmax, resolution=1001):
    xlist = np.linspace(xmin, xmax, n)
    ylist = f(xlist)
    xlist_fine = np.linspace(xmin, xmax, resolution)
    ylist_fine = p_L(xlist_fine, xlist, ylist)
    plt.plot(xlist, ylist, 'ro')
    plt.plot(xlist_fine, ylist_fine)


def annotate_graph():
    ax = plt.gca()
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.legend(['f(x)', 'Interpolated'])

if __name__ == '__main__':
    xlist = np.linspace(0, np.pi, 5)
    ylist = np.sin(xlist)
    verbose_verify(xlist, ylist)
    graph(np.sin, 5, 0, np.pi)
    annotate_graph()
    plt.show()

"""
Sample run:
python Lagrange_poly2.py
         x      Exact     Approx   Difference
  0.000000   0.000000   0.000000     0.000000
  0.785398   0.707107   0.707107     0.000000
  1.570796   1.000000   1.000000     0.000000
  2.356194   0.707107   0.707107     0.000000
  3.141593   0.000000   0.000000     0.000000
"""
