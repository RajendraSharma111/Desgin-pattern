class Person(object):
  def __init__(self):
    self.name = None
    self.gender = None

  def getName(self):
    return self.name

  def getGender(self):
    return self.gender

class Male(Person):
  def __init__(self, name, gender):
    self.name = name
    self.gender = gender

class Female(Person):
  def __init__(self, name, gender):
    self.name = name
    self.gender = gender

class Factory(object):
  def getPerson(self, name, gender):
    if gender == 'M':
      return Male(name, gender)
    if gender == 'F':
      return Female(name, gender)

if __name__ == '__main__':
  factory = Factory()
  male = factory.getPerson("Chetan", "M")
  print (male.getGender(), male.getName())
  female = factory.getPerson("Maya", "F")
  print (female.getGender(), female.getName())
