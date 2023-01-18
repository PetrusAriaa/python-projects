from math import sin, cos

PROBLEM = '2sin(x)+sin(3x)+2cos(x)+1'
print(f"\nPROBLEM:{PROBLEM}")
start = float(input('start: '))
stop = float(input('stop: '))
step_len = float(input('step_length:'))

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