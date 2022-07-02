people = [
    {"name":"Harry","house":"Toronto"},
    {"name":"Cho","house":"Brampton"},
    {"name":"Draco","house":"Milton"}
]

def f(person):
    return person["name"]

people.sort(key=f)

#instead of defining function called F
people.sort(key=lambda person: person["name"])