from oop.cont_bancar import Contbancar

cont1 = Contbancar('Andy S', 'RO001')
cont2 = Contbancar('Crina S', 'RO0002')

cont1.activareCont(7777)
cont2.activareCont(3333)
cont2.activareCont(7777)

cont1.alimentareCont(300)
cont2.alimentareCont(700)
cont2.alimentareCont(300)

cont1.plataCard(500)
cont1.plataCard(300)
cont2.plataCard(100)
cont2.plataCard(200)

cont1.interogareSold()
cont2.interogareSold()

# tema
# clasa Angajat
# nume, prenume, salariu, functie, vechime
# constructor: nume, prenume, salariu, functie, vechime
# metode
# descriere
# marire salariu in functie de vechime
# actualizare vechime (parametru noua vechime)
    # self.vechime = noua_vechime
# daca are vechime sub 5 ani, marim cu 300, peste 5 ani, 500