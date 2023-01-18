from math import sin, cos


# default: 6.664165097862194
def f(x) -> float:
    return 2*sin(x) + sin(3*x) + 2*cos(x) + 1

def Integral_trapezoidal(a, b, step_len) -> float:

    """
    Returns the integral of the trapezoidal rule.
    Parameters
    ----------
    a : float
        lower limit of the integral
    b : float
        upper limit of the integral
    step_len : float
        length of step

    Returns
    -------
    float"""
    return something
    
steps = 0.00001
start = 0
stop = 2

a = start
b = start + step
result = 0

while a < stop:
    curr += (f(a) + f(b))*step/2
    a = b
    b += step

