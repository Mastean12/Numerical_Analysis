def f(x):
    """ Define the function for which we want to find the root. """
    return x ** 3 - 2 * x - 5


def bisection_method(a, b, tol):
    print("\n***SOLVING THE ROOT OF A FUNCTION USING BISECTION METHOD***")
    i = 1
    condition=True
    while condition:
        x = (a + b)/2
        if f(x)<0:
            a=x
        else:
            b=x
        print("iteration", i, "x=", x, "f(x)", f(x))
        if i==tol:
            condition=False
        else:
            condition=True
            i=i+1
    print("The root of the bisection method is:", x)


a = float(input("Enter the lower bound a: "))
b = float(input("Enter the upper bound b: "))
tol = int(input("Enter the tolerance level: "))

root = bisection_method(a, b, tol)
if f(a)*f(b)>0:
    print("Root not found!")
    print("Try another interval...")
else:
    bisection_method(a, b, tol)

