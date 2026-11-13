
#A child class can reuse code from a parent class.
class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()
dog.bark()
#Dog automatically gets the eat() method from Animal.SS