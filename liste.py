# listele in python pot sa contina elemente de diferite tipuri
# au dimensiune dinamica

fructe = ['mar', 'banana', 'portocala', 3, True, 3]

# afisam
print(fructe)

# accesam un element in fucntie de index
print(fructe[1])

# adaugam un element
fructe.append('rosie')

# suprascriem un element
fructe[0] = 'para'

# afisam lista
print(fructe)

# aflam dimensiunea
print(len(fructe))

# scoate si ne returneaza ultimul element
last = fructe.pop()
print('ultimul element:', last)
print('lista', fructe)

# de cate ori apare un element?
print(fructe.count(3))

# extindem lista
fructe_exotice = ['ananas', 'kiwi']
fructe.extend(fructe_exotice)
print(fructe)