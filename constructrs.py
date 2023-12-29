class Defa_con:
    def __init__(self):
        print("This is Default Constructor as it has only one argument")


Defa_con()


class Para_con:
    def __init__(self, ar_1, ar_2):
        self.a = ar_1
        self.b = ar_2
        print(f"This is Parameterized Constructor as it has two arguments {ar_1} and {ar_2}")


obj = Para_con(1, 2)
print(f"{obj.a} is the argument of the object obj for the class Para_con")
print(obj.b)
