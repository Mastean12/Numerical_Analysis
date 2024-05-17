# Newton-Raphson Method
import math

def f(x):
    return x**3 - 3*x - 5

def g(x):
    return 3*x**2 - 3

def newton_Raphson(x0, e, N):
    print('\n\n*** SOLVING THE ROOT OF A FUNCTION USING NEWTON RAPHSON METHOD ***')
    i = 1
    flag = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print("Error! g(x) is zero, try a different initial guess...")
            break
        x1 = x0 - f(x0) / g(x0)
        print("Iteration-%d, x1 = %0.6f and f(x1) = %0.6f" % (i, x1, f(x1)))
        x0 = x1
        i += 1

        if i > N:
            flag = 0
            break

        condition = abs(f(x1)) > e

    if flag == 1:
        print("\nRequired root is: %0.8f" % x1)
    else:
        print("\nNot convergent.")

x0 = float(input("Enter a number: "))
e = float(input("Enter tolerable error: "))
N = int(input("Enter maximum number of iterations: "))
newton_Raphson(x0, e, N)





