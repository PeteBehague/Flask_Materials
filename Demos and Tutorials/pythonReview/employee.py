
class Employee():
    def __init__(self, id=-1, firstname="anon", lastname="smith", age=20):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self._age = age

    def __str__(self):
        return f"with an id of {self.id}: {self.firstname} {self.lastname} is {self._age} years old"

    def birthday(self):
        self._age += 1

    def get_credentials(self):
        return f"{self.firstname[0:1].upper()} {self.lastname.capitalize()}"

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if new_age < 0 or new_age > 200:
            new_age = 0
        self._age = new_age

    age = property(get_age, set_age)




