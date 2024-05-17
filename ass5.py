# Defining Function
def f(x):
    return x**3-5*x-9

# Implementing False Position Method
def false_Position(x0,x1,e):
    i = 1
    print('\n\n*** SOLVING THE ROOT OF A FUNCTION USING FALSE POSITION METHOD ***')
    condition = True
    while condition:
        x2 = x0 - (x1-x0) * f(x0)/( f(x1) - f(x0) )
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (i, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        i = i + 1
        condition = abs(f(x2)) > e

    print('\nRequired root is: %0.8f' % x2)


# Input Section
x0 = input('Enter First Value: ')
x1 = input('Enter Second Value: ')
e = input('Tolerable Error: ')


# Checking Correctness of initial guess values and false positioning
if f(x0) * f(x1) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    false_Position(x0,x1,e)