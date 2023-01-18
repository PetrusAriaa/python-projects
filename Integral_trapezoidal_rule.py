from math import sin, cos

PROBLEM = '2sin(x)+sin(3x)+2cos(x)+1'
step_len = 0.5
start = 0
stop = 2
print(f"\nPROBLEM:{PROBLEM}")
print(f'starting point: {start}')
print(f'end point: {stop}')
print(f'length of step: {step_len}')

# default: 6.664165097862194
def f(x) -> float:
    return 2*sin(x) + sin(3*x) + 2*cos(x) + 1

def Integral_trapezoidal(start, stop, step_len) -> float:
    a = start
    b = start + step_len
    result = 0
    while b <= stop:
        result += (f(a) + f(b))*step_len/2
        a = b
        b += step_len
    return result

result = Integral_trapezoidal(start, stop, step_len)
print(f'\n>> Integral operation result: {result}')
