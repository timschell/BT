class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, {self.name}")

p = Person("Bob")
p.say_hello()
