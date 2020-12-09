class Point():
    def __init__(self, x, y):
        self.x=x
        self.y=y

p=Point(4,8)
print(p.x)
print(p.y)

class Flight():
    def __init__(self, capacity):
        self.capacity=capacity
        self.passengers=[]

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        else:
            self.passengers.append(name)
            return True

    def open_seats(self):
        return self.capacity-len(self.passengers)

flight=Flight(3)
people=["Harry","Ron","Hermione","Ginny"]
for persons in people:
    success=flight.add_passenger(persons)
    if success:
        print(f"Added {persons} successfully")

    else:
        print("Not added successfully")