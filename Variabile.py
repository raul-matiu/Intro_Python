# variabila = zona din memorie care tine anumite date
# variabila = o cutiuta in care punem valori

# am declarat si initializat variabila marca
marca_masina = 'Volvo'
model_masina = 'XC 60'

# nu putem sa punem spatiu in numele variabilei
# o variabila incepe cu litera mica

# loosely typed - nu trebuie sa specificam tipurile de date

print(f'Am cumparat o masina: {marca_masina}')
print(f'Este modelul : {model_masina}')

# suprascriere
model_masina = 'XC 60 facelift'

print(f'Am cumparat o masina: {marca_masina}')
print(f'Este modelul : {model_masina}')

nume = 'Matiu'
prenume = 'Raul'
varsta = 41
print('nume' + ' ' + 'prenume')
print(f'{nume} {prenume} are varsta de {varsta} ani')