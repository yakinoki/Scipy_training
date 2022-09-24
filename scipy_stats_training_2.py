from scipy import stats
from scipy import integrate
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

def h(x,y):
    if 0 <= x+y <=1 and 0 <= x <= 1/2:
        return 4*x*(x-y)
    else:
        return 0

print(integrate.nquad(h, [[-np.inf, np.inf],[-np.inf, np.inf]]))