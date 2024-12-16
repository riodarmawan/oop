class Staff:
    def __init__(self,name,age,position):
        self.name = name
        self.age = age
        self.position = position

    def introduce(self):
        return f"My name is {self.name}, i am {self.age} years old and i am a {self.position}"

class Doctor(Staff):
    def __init__(self,name,age,position,specialization):
        super().__init__(name,age,position)
        self.specialization = specialization

    def introduceDocter(self):
        introduceDocter = super().introduce()
        return f"{introduceDocter} with specialization {self.specialization}" 

class Nurse(Staff):
    def __init__(self, name, age, position,departement):
        super().__init__(name, age, position)
        self.departement = departement
    
    def introNurse(self):
        introNurse = super().introduce()

        return f"{introNurse} in departement {self.departement}"



x = Doctor("x","22","docter","jantung")
print(x.introduceDocter())

y = Nurse("x","22","Perawat","Anak")
print(y.introNurse())