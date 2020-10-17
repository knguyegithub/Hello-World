import os

cls = lambda: os.system('cls')

def fahrenheit_to_celsius(temperature):
    formula = (int(temperature) - 32) * 5/9
    return round(formula)

def celsius_to_fahrenheit(temperature):
    formula = (int(temperature) * 9/5) + 32
    return round(formula)

def main():
    print("Temperature Conversion.\n 1.) Fahrenheit to Celsius - Type \"1\"\n 2.) Celsius to Fahrenheit - Type \"2\"\n Exit - Type \"3\"")
    option = input("Select Option: ")
    if option == "1":
        val = input("Enter Temperature in °F: " )
        temperature = fahrenheit_to_celsius(val)
        cls()
        print(str(temperature) + "°C")
        main()
    elif option == "2":
        val = input("Enter Temperature in °C: " )
        cls()
        temperature = celsius_to_fahrenheit(val)
        print(str(temperature) + "°F")
        main()
    elif option == "3":
        cls()
        print("Goodbye!")
        exit()
    else:
        cls()
        print("ERROR: Wrong input. Please enter \"1\" or \"2\".")
        main()

if __name__ == "__main__":
    main()
