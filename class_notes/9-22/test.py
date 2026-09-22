

class Test():
    def __init__(self, x):
        print(" In the init")
        self.x = x

    def foo(self):
        print(" In foo")
        print(self.x)

    def __mul__(self, other):
        pass

    def __len__(self):
        return self.x

    def __eq__(self, other):
        return True

a = Test(10)
a.foo()

a == a
len(a)

