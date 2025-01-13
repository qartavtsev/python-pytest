from operator import length_hint


class Person:
    # create class
    def __init__(self, name):
        # init parametrs
        self.name = name
        self.hp = 10
        self.mdef = 2
        self.pdef = 3

    def take_true_damage(self, count):
        # take true damage
        self.hp = self.hp - count
        pass

    def take_magic_damage(self, count):
        # take magic damage
        self.hp = self.hp - count / self.mdef
        pass

    def take_melee_damage(self, count):
        # take melee damage
        self.hp = self.hp - count / self.pdef
        pass

    def test_take_ranged_damage(self, count, length):
        # take ranged damage
        # length - between target and archer
        k = (60 - length) / 100
        self.hp = self.hp - count * k / self.pdef
        pass



if __name__ == '__main__':
    # start only on compile this page
    alex_person = Person('Alex')
    print(alex_person.name)
    print(alex_person)
    alex_person.take_true_damage(1)
    print(alex_person.hp)