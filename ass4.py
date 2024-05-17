# Defining Function
def f(x):
    return x ** 3 - 5 * x - 9


# Implementing Secant Method

def secant(x0, x1, e, N):
    print('\n\n*** SOLVING THE ROOT OF A FUNCTION USING SECANT METHOD ***')
    i = 1
    condition = True
    while condition:
        if f(x0) == f(x1):
            print('Divide by zero error!')
            break

        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % ( i, x2, f(x2)))
        x0 = x1
        x1 = x2
        i = i + 1

        if i > N:
            print('Not Convergent!')
            break

        condition = abs(f(x2)) > e
    print('\n Required root is: %0.8f' % x2)


# Input Section
x0 = float(input('Enter First Value: '))
x1 = float(input('Enter Second Value: '))
e = float(input('Enter Tolerable Error: '))
N = int(input('Enter Maximum Step: '))



# Starting Secant Method
secant(x0, x1, e, N)
