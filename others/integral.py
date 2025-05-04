# pip install latexify-py
#import latexify
from scipy import integrate
from functools import partial
import numpy as np
import warnings


warnings.filterwarnings('ignore',category=integrate.IntegrationWarning)

def f(x):
    if 0 <= x <= 6:
        return 3*x
    else:
        return 0

#1つめの返り値が積分値。2つめは推定誤差。
print(integrate.quad(f, 1, 3))

@latexify.function
def h(x, y):
    if 0 <= x+y <=1 and 0 <= x <= 1/2:
        return 4*x*(x-y)
    else:
        return 0

h

print(integrate.nquad(h, [[-np.inf, np.inf],[-np.inf, np.inf]]))

def h_x(x):
    return integrate.quad(partial(h, x), -np.inf, np.inf)[0]

def h_y(y):
    return integrate.quad(partial(h, y=y), -np.inf, np.inf)[0]
