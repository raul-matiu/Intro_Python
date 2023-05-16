def add():
    a = float(input('introduceti un numar. '))
    b = float(input('introduceti un alt numar. '))
    print(a + b)


def subtraction():
    a = float(input('introduceti un numar. '))
    b = float(input('introduceti un alt numar. '))
    print(a - b)


def multiply():
    a = float(input('introduceti un numar. '))
    b = float(input('introduceti un alt numar. '))
    print(a * b)


def divide():
    a = float(input('introduceti un numar. '))
    b = float(input('introduceti un alt numar. '))
    print(a / b)


operation = input('Va rugam scrieti +, - , *, sau /')
if operation == '+':
    add()
elif operation == '-':
    subtraction()
elif operation == '*':
    multiply()
elif operation == '/':
    divide()
else:
    print('Aceasta operatie nu este disponibila!')