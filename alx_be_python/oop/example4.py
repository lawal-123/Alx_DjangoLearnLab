class Animal:
    def __init__(self, eat, sleep):
        self.eat = eat
        self.sleep = sleep
    def __str__(self):
        return f"Animal {self.eat} and {self.sleep}"
class Dog(Animal):
    def__init__(self, eat, sleep, bark):
        super().__init__(eat, sleep)
        self.bark = bark