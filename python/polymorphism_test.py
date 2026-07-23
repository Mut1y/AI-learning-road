class Dog:


    def speak(self):

        print("汪汪")



class Cat:


    def speak(self):

        print("喵喵")



class Person:


    def speak(self):

        print("你好")



def make_speak(obj):

    obj.speak()



dog = Dog()

cat = Cat()

person = Person()


make_speak(dog)

make_speak(cat)

make_speak(person)