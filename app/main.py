class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"


def create_person_list(people_data):
    # ✅ Resetar o estado compartilhado para evitar dados obsoletos
    Person.people = {}

    # ✅ Criar instâncias usando list comprehension
    people = [Person(p['name'], p['age']) for p in people_data]

    # ✅ Estabelecer vínculos mútuos entre cônjuges
    for data in people_data:
        person = Person.people[data['name']]

        wife_name = data.get('wife')
        if wife_name:
            wife = Person.people.get(wife_name)
            if wife:
                if person.wife is None:
                    person.wife = wife
                if wife.husband is None:
                    wife.husband = person

        husband_name = data.get('husband')
        if husband_name:
            husband = Person.people.get(husband_name)
            if husband:
                if person.husband is None:
                    person.husband = husband
                if husband.wife is None:
                    husband.wife = person

    return people
