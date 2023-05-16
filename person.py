class Person:
    def __init__(self, prenume, nume, sanatate, status):
        # atributele initialize

        self.prenume = prenume
        self.nume = nume
        self.sanatate = sanatate
        self.status = status

    def introduce(self):
        "Toti oamenii se prezinta"
        print('Buna ziua, ma numesc {} {}.'.format(self.prenume, self.nume))

    def emote(self):
        emotion = random.randrange(1,3)
        if emotion == 1:
            print('{} este fericit azi.'.format(self.prenume))
        elif emotion == 2:
            print('{} este trist acum.'.format(self.prenume))
    def status_change(self):
        if self.sanatate == 100:
            print('{} este sanatos tun!'.format(self.prenume))
        elif self.sanatate >= 76:
            print('{} este un pic obosit azi.'.format(self.prenume))
        elif self.sanatate >=51:
            print('{} se simte rau.'.format(self.prenume))
        elif self.sanatate >= 40:
            print('{} merge la doctor'.format(self.prenume))
        else:
            print('{} este inconstient.'.format(self.prenume))

Maria = Person('Maria', 'Magdalena', 95, status=True)
Rey = Person('Rey', 'Jones', 88, status=False)
Lee = Person('Lee', 'Williams', 72, status=True)

print('{} este prietena mea? {}'.format(Maria.prenume, Maria.status))
print('{} este prietenul meu? {}'.format(Rey.prenume, Rey.status))

Maria.introduce()
Rey.introduce()
Lee.introduce()

Maria.status_change()
Rey.status_change()
Lee.status_change()

class Enemy(Person):
    def __init__(self, weapon, prenume, nume, sanatate, status):
        super().__init__(prenume, nume, sanatate, status)
        self.weapon = weapon

# polimorfism
    def introduce(self):
        print('You are my mortal enemy!!!')

    def hurt(self, other):
        if self.weapon == 'rock':
            other.sanatate -= 10
        elif self.weapon == 'stick':
            self.sanatate -= 5
        print(other.sanatate)

    def insult(self, other):
        if other.sanatate <= 80:
            print('{}, tu esti obosit si slabit'.format(other.prenume))

    def steal(self, other):
        print('ha ha ha, {}, ti-am luat lucrurile!'.format(other.prenume))
        if other.status == True:
            other.status = False

Alex = Enemy('rock', 'Alex', 'Wayne', 75, status = False)
Alex.introduce()

Alex.hurt(Maria)
Alex.insult(Rey) #nu ar trebui sa se printeze nimic
Alex.insult(Lee)
Alex.steal(Rey)
