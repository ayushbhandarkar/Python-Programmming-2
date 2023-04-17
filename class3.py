class Car:
    name = ""
    year = 0

    def get_details(self):
        self.name = input(" Enter the car name : ")
        self.year = int(input(" Enter the Launching year "))

    def show_details(self):
        print(" Car name : ", self.name)
        print(" Car launching year : ", self.year)


honda = Car()
print("\n \t\t\t Enter the details of Honda : ")
honda.get_details()

maruti = Car()
print("\n \t\t\t Enter the details of maruti : ")
maruti.get_details()

choice = input(" Enter your choice : ")
if choice == "honda":
    honda.show_details()
elif choice == "maruti":
    maruti.show_details()
else:
    print(" Check your input ")