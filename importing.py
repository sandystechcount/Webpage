# book flight having a capacity of 4, return the list of attendees who succcessully booked and who could'nt

class Person():

    # intialize flight capacity and get attendees list

    def __init__(self, capacity) :
        self.capacity = capacity
        self.passenger = []

    # Book tickets based on the availability

    def booking(self, name) :
        if not self.checkLimit():
            return False
        else:
            self.passenger.append(name)
            return True

    # check the booking limit

    def checkLimit(self):
       return self.capacity-len(self.passenger)

    # Create class object, pass names and print the result

person = Person(4)
people = ["Harry", "Ron", "Hermione", "Ginny", "Bourbon"]
personSorted = people.sort()
for i in personSorted :
    if person.booking(i):
         print(f"Added {i} to flight successfully")
    else :
        print(f"No available seats for {i}")

   