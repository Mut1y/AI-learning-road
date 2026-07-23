class Animal:


    def speak(self):

        print("动物发出声音")



class Dog(Animal):


    def speak(self):

        print("汪汪")



class Cat(Animal):


    def speak(self):

        print("喵喵")



dog = Dog()

cat = Cat()


dog.speak()

cat.speak()