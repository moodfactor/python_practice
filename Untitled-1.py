class MixedNames:
    data = "spam"

    def __init__(self, value) -> None:
        self.data = value

    def display(self):
        print(self.data, MixedNames.data)


x = MixedNames(1)
y = MixedNames(2)
x.display()
y.display()
print(MixedNames.display(y))
print(MixedNames.data)


class NextClass:
    def printer(self, text):
        self.message = text
        print(self.message)


x = NextClass()
x.printer("instance call")
x.message

NextClass.printer(x, "class call")
x.message

print(NextClass.printer(x, "class call"))
print(x.message)
