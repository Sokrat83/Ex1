class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)

class Manager(Person):

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent+bonus)



bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay=100000)
print(bob)
print(sue)
print(bob.lastName(), sue.lastName())
sue.giveRaise(.10)
print(sue.pay)

tom = Manager('Tom Jones', 'mgr', 50000)
tom.giveRaise(.10)
print(tom.lastName())
print(tom)


