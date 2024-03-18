class Person:
    def __init__(self, name, age, gender):
        self.name = name;
        self.age = age;
        self.gender = gender;
    
    
    def introduce(self):
        print("My good name is {self.name}. I am {self.age} years and I'm {self.gender}")
    
    person1 = Person("Daniel", 0, "Male");
    
    person1.introduce();