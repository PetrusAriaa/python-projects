from numpy import array
# Fibonacci matrix
# [U(n+1)] = [0 1]  [U(n)]
# [U(n+2)]   [1 1]  [U(n+1)]
first_number = 7
second_number = 7
print(array([first_number, second_number]))

for i in range(9):
    myMatrix=array([second_number*1,first_number*1+second_number*1])
    first_number = myMatrix[0]
    second_number = myMatrix[1]
    print(myMatrix)
