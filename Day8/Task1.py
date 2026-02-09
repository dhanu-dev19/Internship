from abc import ABC, abstractmethod

# Abstract Class
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    # Normal method
    def sleep(self):
        print("Animal is sleeping")


class Dog(Animal):
    def sound(self):
        print("Bark")


class Cat(Animal):
    def sound(self):
        print("Meow")


class Cow(Animal):
    def sound(self):
        print("Moo")

dog = Dog()
cat = Cat()
cow = Cow()

dog.sound()
dog.sleep()

cat.sound()
cat.sleep()

cow.sound()
cow.sleep()
