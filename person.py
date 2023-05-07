class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self) -> str:
        return f"[Person: {self.name}, {self.pay}]"

    def __str__(self) -> str:
        return f"{self.name}"


bob = Person("Bob Smith")
print(bob.__dict__.keys())
o = dir(bob)
print(list(a for a in o if not a.startswith("__")))


class Manager(Person):
    def __init__(self, name, job=None, pay=0):
        Person.__init__(name, "mgr", pay)

    def giveRaise(self, percent, bonus=0.10):
        # Person.giveRaise(self, percent+bonus)
        Person.giveRaise(self, percent + bonus)

    def __repr__(self) -> str:
        return super().__repr__() + f"\nManager: {self.pay}"


if __name__ == "__main__":
    bob = Person("Bob Smith")
    sue = Person("Sue Jones", job="dev", pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(0.10)
    print(sue)
