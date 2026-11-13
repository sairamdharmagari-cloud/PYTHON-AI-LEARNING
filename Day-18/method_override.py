#A child class can provide its own version of a parent method.
class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog says: Woof!")


animal = Animal()
dog = Dog()

animal.sound()
dog.sound()#The Dog version replaces the inherited sound() behavior.S