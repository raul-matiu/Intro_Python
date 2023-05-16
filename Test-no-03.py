def user_info(nume, varsta, oras):
    '''Aceasta functie afiseaza numele, varsta si orasul, de la un argument furnizat functiei'''
    print('{} a implinit {} ani si a plecat in vizita spre {}'.format(nume, varsta, oras))

user_info('Alin', 40, 'Constanta')

# daca atribuim user_info(40, 'Constanta') se va afisa o eroare 'oras' chiar daca ne lipseste argumentul 'nume'

def user_info(nume, varsta= 0, oras= 'Bucuresti'):
    '''Aceasta functie afiseaza numele, varsta si orasul, de la un argument furnizat functiei'''
    print('{} a implinit {} ani si a plecat in vizita spre {}'.format(nume, varsta, oras))

user_info(varsta= 35, nume= 'Costica')

def application (nume, prenume, email, angajator,*args, **kwargs):
    print('{} {} lucreaza pentru {}. Il puteti contacta pe adresa de mail {}.'.format(nume, prenume, angajator, email))

application('Ion', 'Vasile', 'ion.vasile@vasion.com','Vasion.org', 10000, data_angajarii= 'noiembrie 2022')