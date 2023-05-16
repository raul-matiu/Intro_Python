# masini pe piata auto
marca_masina01 = 'Skoda'
model_masina01 = 'Scala'

marca_masina02 = 'VW'
model_masina02 = 'Golf'

marca_masina03 = 'Hyundai'
model_masina03 = 'i30'

# pret la valorea de nou
pret_noua = 15000

# pret second hand
pret_second = 12000

print(f'Masina anului in Romania este: {marca_masina01} {model_masina01}')
print(f'Pretul de nou al {marca_masina01.upper()} {model_masina01.upper()} este de {pret_noua} euro')
print(f'Topul vanzarilor de masini in Romania este: 1.{marca_masina02} 2.{marca_masina01} 3.{marca_masina03}')
print(f'Masina second cu cea mai buna rata de rentabilitate este {marca_masina02} {model_masina02}, avand un pret mediu de vanzare de aprox {pret_second} euro ')
print(len(marca_masina01))

print('{} este a treia cea mai vanduta masina a producatorului {}'.format(model_masina03, marca_masina03))

# functia adunare

def addition():
    x = 2500.9
    y = 75222.02
    print(x + y)

addition()


# scratch variables

def addition():
    x = int(input('introduceti un numar. '))
    y = int(input('va rugam introduceti inca un numar. '))
    print(x + y)

addition()
