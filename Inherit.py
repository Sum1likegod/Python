# Inheritance

class Grand_Father:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'This is Grandfather\'s details {self.name} and {self.age}')


class Father(Grand_Father):
    def show_2(self):
        print(f'This is Father\'s details {self.name} and {self.age}')


ex_inh = Grand_Father('Sushil', 60)
ex_inh.show()
ex_inh_2 = Father('Ajay', 45)
ex_inh_2.show_2()
