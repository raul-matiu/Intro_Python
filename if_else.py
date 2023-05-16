piesa_faina = True

print('pornim radio')
if piesa_faina ==  True:
    print('dam mai tare')
    print('fredonam')
print('oprim radio')

#if else
# daca un numar este par printam acest lucru
# altfel printam impar

nr = 3
# ce inseamna par se imaprte exact la 2
# ce inseaman ca se imparte exact la 2 ? ne da restul 0
if nr % 2 == 0:
    print('numar par')
else:
    print('numar impar')

# este un numar pozitiv ?
if (nr > 0):
    print('pozitiv')
else:
    print('nr nu este pozitiv')

#if, else if, else
# cum ne saluta un robotel in functie de ora

# luam date de la tastaura
# ne asiguram ca sunt transformate din str in int
# ora = int(input('Introdu ora'))
# if ora <0:
#     print('Ora invalida, ora negativa')
# elif ora <= 11:
#     print('Buna dimineata!')
# elif ora <= 18:
#     print('Buna ziua!')
# elif ora <= 21:
#     print('Buna seara!')
# elif ora <= 24:
#     print('Noapte buna!')
# else:
#     print('Ora invalida, ora mai mare decat 24')
# CTRL + / : selectezi/ deselectezi o parte din program
# robotel telefonic
optiunea = int(input('alege o optiune'))
if optiunea == 0:
    print('meniu anterior')
elif optiunea == 1:
    print('ati ales meniu in limba romana')
elif optiunea == 2:
    print('you choose english')
else:
    print('nu am identificat optiunea, mai incearca')