from math import sin, cos

PROBLEM = '2sin(x)+sin(3x)+2cos(x)+1'
start = 0
stop = 2
print(f"\nPROBLEM:{PROBLEM}")
print(f'starting point: {start}')
print(f'end point: {stop}')

# default: 6.664165097862194
def f(x) -> float:
    return 2*sin(x) + sin(3*x) + 2*cos(x) + 1

def Integral_simpsons_one_per_three_rule(start, stop) -> float:
    mid = (stop+start)/2
    result = (mid/3)*(f(start) + f(stop) + 4*f(mid))
    return result

result = Integral_simpsons_one_per_three_rule(start, stop)
print(f'\n>> Integral operation result: {result}')