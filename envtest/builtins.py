import numpy as np
from scipy.ndimage import gaussian_filter
from scipy import misc
import math


__all__ = ['rand_array', 'smooth_image', 'my_mat_solve', 'math_method']


def rand_array(shape):
    return np.random.rand(*shape)

def smooth_image(a, sigma=1):
 return gaussian_filter(a, sigma=sigma)

def my_mat_solve(A, b):
    return A.inv()*b

def math_method(x):
    return x*math.pi
