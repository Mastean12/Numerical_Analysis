import math

def f(x):
    return x**3 + x**2 - 1

# Re-writing f(x)=0 to x = g(x)
def g(x):
    return 1 / math.sqrt(1 + x)

# Implementing Fixed Point Iteration Method
def fixed_Point_Iteration(x0, e, N):
    print('\n\n*** SOLVING THE ROOT OF A FUNCTION USING FIXED POINT ITERATION ***')
    i = 1
    flag = 1
    condition = True
    while condition:
        x1 = g(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (i, x1, f(x1)))
        x0 = x1
        i += 1

        if i > N:
            flag = 0
            break

        condition = abs(f(x1)) > e

    if flag == 1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')

# Input Section
x0 = float(input('Enter Guess: '))
e = float(input('Tolerable Error: '))
N = int(input('Maximum Step: '))

# Starting Fixed Point Iteration Method
fixed_Point_Iteration(x0, e, N)
