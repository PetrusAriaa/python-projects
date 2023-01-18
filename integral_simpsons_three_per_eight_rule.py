from math import sin, cos

PROBLEM = '2sin(x)+sin(3x)+2cos(x)+1'
print(f"\nPROBLEM:{PROBLEM}")
start = float(input('start: '))
stop = float(input('stop: '))

# default: 6.664165097862194
def f(x) -> float:
    return 2*sin(x) + sin(3*x) + 2*cos(x) + 1

def Integral_simpsons_one_per_three_rule(start, stop) -> float:
    step_length = (stop+start)/3
    result = (3*step_length/8)*(f(start) + f(stop) + 3*f(start+step_length) + 3*f(start+(2*step_length)))
    return result

result = Integral_simpsons_one_per_three_rule(start, stop)
print(f'\n>> Integral operation result: {result}')