class Swordsman:
    people = 'people'


    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.health_points = health_points
        self.nickname = nickname
        self.superpower = superpower
        self.catchphrase = catchphrase


    def n(self):
        print(f'Wanted: {self.name}')


    def h(self):
        self.health_points *= 2


    def __str__(self):
        return f'Nickname: {self.nickname}' \
               f'Power: {self.superpower}' \
               f'Health: {self.health_points}'


    def __len__(self):
        return len(self.catchphrase)


hero = Swordsman('Kirigaya', 'Kirito\n', 'fencing\n', 14000, 'Я скорее погибну вместе с другим человеком, чем буду просто стоять и смотреть, как он погибает один')
hero.n()
hero.h()
print(hero)
print(f'Catchphrase: {len(hero.catchphrase)}')


class Swordsman_2(Swordsman):
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def h(self):
        abc = self.health_points ** 2
        self.health_points = abc

    def f(self):
        self.fly = True

    def phrase(self):
        print('fly in the True_phrase')

hero_2 = Swordsman_2('Asuna', 'Asuna\n', 'fencing\n', 13000, 'Жить — значит сохранять и передавать мысли...')

hero_2.h()
print(hero_2)
print(f'Damage: {hero_2.damage}')
hero_2.f()
print(f'Fly: {hero_2.fly}')
hero_2.phrase()


class Swordsman_3(Swordsman):
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def h(self):
        abc = self.health_points ** 2
        self.health_points = abc

    def f(self):
        self.fly = True

    def phrase(self):
        print('fly in the True_phrase')

hero_3 = Swordsman_3('Ryotaro', 'Klein\n', 'fencing\n', 13000, '-')

hero_3.h()
print(hero_3)
print(f'Damage: {hero_3.damage}')
hero_3.f()
print(f'Fly: {hero_3.fly}')
hero_3.phrase()

class Villain(Swordsman_3):
    monster = 'monster'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)

    def gen_x(self): ...

    def crit(self):
        print(f'Crit dm: {self ** 2}')

antihero = Villain('Akihiko Kayaba', 'Hitkliv\n', 'liberator\n', '15000', 'это игра, но в нее невозможно играть')

print(antihero)
antihero.gen_x()
Villain.crit(hero_2.damage)

