#A Python Class is essentially a template for a new type of object that can store information and perform actions.
#we use the keyword self to represent the object we are currently working with. 
#self should be the first argument for any method within a Python class.
class Point():
    def __init__(self, input1, input2): 
        self.x = input1
        self.y = input2


p = Point(2,8)
print(p.x)
print(p.y)

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    succes = flight.add_passenger(person)
    if succes:
        print(f"Added {person} to flight succefully.")
    else:
        print(f"No availabe seats for {person}")