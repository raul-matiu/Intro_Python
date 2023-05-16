def printGreeting():
    print('Buna ziua ! Bine ati venit!')

def printGreetingByName(nume, prenume):
    print(f'Buna ziua {nume} {prenume}! ')

def mediaNr(a, b, c):
    return (a + b + c) / 3

def piValue():
    return 3.14

# exercitiu
# daca pers e majoara, altfel false
def verificareMajor(varsta):
    if varsta >= 18:
        return True
    else:
        return False



# zona de apelare desktop
printGreeting()
printGreeting()
printGreetingByName('Sinpetrean', 'Andy')
printGreetingByName('Sinpetrean', 'Andu')
printGreetingByName('Sinpetrean', 'Andra')
print(mediaNr(3, 3, 4))
print(piValue())
print(verificareMajor(17))

age = int(input('introduceti varsta dvs'))
if verificareMajor(age):
    print('Cont creat. Bine ai venit in aplicatie.')
else:
    print('Nu ai varsta minima necesara (18) pt a aparia')

# oop
# variabile => atribute, proprietati sau fields
# functii => metode