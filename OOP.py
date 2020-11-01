class Person:
    def __init__(self,person_name):
        self.name = person_name

    def get_name(self):
        return self.name


a_person = Person("Shaikat")
b_person = Person("Alpha")


print(a_person.get_name())
print(b_person.get_name())

class Person:
    def __init__(self,person_name,date_of_birth,ht):
        self.name = person_name
        self.dob = date_of_birth
        self.height = ht

    def get_summary(self):
        return f"Name:{self.name} | Date of Birth:{self.dob} | Height:{self.height}"

Nid1=Person("Shaikat","25.07.1999","5.9")

print(Nid1.get_summary())



class Person:
    def __init__(self,person_name,date_of_birth,ht):
        self.name = person_name
        self.dob = date_of_birth
        self.height = ht 

    def get_summary(self):
        return f"Name:{self.name} | Date of Birth:{self.dob} | Height:{self.height}"


    def set_name(self,new_name):
        self.name = new_name


Nid1=Person("Shaikat","25.07.1999","5.9")
Nid1.set_name("Shaikat Barua")

print(Nid1.get_summary())


class Person:
    def __init__(self, person_name: str, year_of_birth: int, ht_inches: int = None):
        self._name = person_name
        self._year = year_of_birth
        self._height = ht_inches


    # def get_summary(self):
    #     return f"Name:{self._name} | Birth Year:{self._year} | Height:{self._height}"
        

    def get_year_of_birth(self):
        return self._year

    def get_summary(self):
        return f"Name:{self._name} | Birth Year:{self._year} | Height:{self._height}"


person_list = [Person("Alpha",1992,6),
Person("Harm",1990,5),
Person("Grim Reaper",1970),
Person("Buzz",1972,4),
Person("Logan",1980),
Person("Jack",1981,5),
Person("Fuzz",1985),
Person("Duke",1998)]


for person in person_list:
    if person.get_year_of_birth() >= 1980:
        print(person.get_summary())

