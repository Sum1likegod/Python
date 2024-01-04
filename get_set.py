#Getters And Setters

class Get_set:
  def __init__(self,my_age):
    self.my_age = my_age

  @property              #for getter staement start it with @property
  def get_age(self):
    return 11*self.my_age

  @get_age.setter        #for setter statement start it with @get_age.setter
  def set_age(self,new_age):
    self.my_age = new_age-10
    print('This is my age after 10 years',new_age)

  def show_age(self,my_age_1):
    self.my_age = my_age_1
    print(my_age_1)
    return my_age_1

age = Get_set(2)
print('This is my current age',age.get_age)
age.set_age = 32 