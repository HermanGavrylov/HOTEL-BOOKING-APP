import pandas

df = pandas.read_csv("hotels.csv")

class Hotel:

    def __init__(self, id):
        pass

    def available(self):
        pass

    def view(self):
        pass

    def book(self):
        pass


class Reservation:

    def __init(self, customer_name, hotel_object):
        pass

    def generare(self):
        pass


print(df)
id = input("Enter the id of the hotel: ")
hotel = Hotel(id)

if hotel.available:
    hotel.book()
    name = input("Enter your name: ")
    reservation = Reservation(name, hotel)
    print(reservation.generate())
else:
    print("Hotel is not free.")
