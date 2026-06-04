from main import Car

class CarTestRun:

    def test_car(self):
        year = int(input("Enter the year model of your car:\n"))
        make = input("\nEnter the make of your car:\n")
        race_car = Car(year, make)

        print(f"\nAccelerating your {year} {make} 5x! Fasten your seatbelts!\n")

        for i in range(5):
            race_car.accelerate()
            print(f"Speedometer: {race_car.get_speed()} kph")

        print(f"\nThe fun part is over! Your car is now braking 5x.\n")

        for i in range(5):
            race_car.brake()
            print(f"Speedometer: {race_car.get_speed()} kph")

        print(f"\nThe ride is now over! Your last recorded speed was {race_car.get_speed()}!\n")

my_car = CarTestRun()
my_car.test_car()