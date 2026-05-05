#molde de uma pessoa
class Person:
    #vamos criar um método, método é uma função que pertence a essa classe
    def __init__(self, name, age, eating=False, speaking=False):
        self.name = name
        self.age = age
        self.eating = eating
        self.speaking = speaking

    def speak(self, comment):
        if self.eating:
            print(f'{self.name} is eating.')
            return
        
        else:
            print(f'{self.name} is speaking about {comment}')
            self.speaking = True

    def stop_speaking(self):
        if not self.speaking:
            print(f'{self.name} isnt speaking.')
            return
        
        print(f'{self.name} is not speaking')
        self.speaking = False

    def eat(self, fruit):
        if self.eating:
            print(f'{self.name} is eating.')
            return
        
        if self.speaking:
            print(f'{self.name} cant speak while eating')
            return
        
        print(f'{self.name} is eating {fruit}')
        self.eating = True

    def stop_eating(self):
        if not self.eating:
            print(f'{self.name} is not eating.')
            return
        
        print(f'{self.name} isnt eating.')
        self.eating = False