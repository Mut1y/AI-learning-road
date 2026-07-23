class Animal:


    def eat(self):

        print("正在吃东西")



class Dog(Animal):


    def bark(self):

        print("汪汪叫")



dog = Dog()


dog.eat()

dog.bark()