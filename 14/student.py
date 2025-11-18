from human import Human

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{super().__str__()}, Record book: {self.record_book}'

    def __eq__(self, other): #comparsion
        if not isinstance(other, Student):
            return False
        return str(self) == str(other)


    def __hash__(self):
        return hash(str(self))