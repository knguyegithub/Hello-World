import os
import time
import math
cls = lambda: os.system('cls')

def delay(sec):
    time.sleep(sec)

def Triangle(): 
    # area = (b * h) / 2
    base = input("Length of base: ")
    height = input("Length of height: ")
    area = (int(base) * int(height)) / 2
    cls()
    print("Area of triangle = " + str(round(area,2)) + "²")
    delay(5)
    return main() 

def Square():
    # area = s^2
    s = input("Enter side length: ")
    area = int(s)**2
    cls()
    print("Area of square = " + str(round(area,2)) + "²")
    delay(5)
    return main()

def Pentagon():
    # area = 1/4 * (sqrt(5 * (5 + 2 * sqrt(5)))) * s^2
    s = input("Enter side length: ")
    cls()
    area = 1/4 * (math.sqrt(5 * (5 + 2 * math.sqrt(5)))) * int(s)**2
    print("Area of pentagon ≈ " + str(round(area,2)) + "²")
    delay(5)
    return main()

def Hexagon():
    # area = ((3 * sqrt(3)) / 2) * s^2
    s = input("Enter side length: ")
    cls()
    area = ((3 * math.sqrt(3)) / 2) * int(s)**2
    print("Area of hexagon ≈ " + str(round(area,2)) + "²")
    delay(5)
    return main()

def Heptagon():
    # area = 7/4 * s^2 * cot(pi/7)
    s = input("Enter side length: ")
    cls()
    x = math.pi / 7
    cot_x = 1/math.tan(x) 
    area = 7/4 * int(s)**2 * cot_x
    print("Area of heptagon ≈ " + str(round(area,2)) + "²")
    delay(5)
    return main()

def Octagon():
    # area = 2 * (1 + sqrt(2)) * s^2
    s = input("Enter side length: ")
    cls()
    area = 2 * (1 + math.sqrt(2)) * int(s)**2
    print("Area of octagon ≈ " + str(round(area,2)) + "²")
    delay(5)
    return main()

def Nonagon():
    # area = 9/4 * s^2 * cot(pi/9)
    s = input("Enter side length: ")
    cls()
    x = math.pi / 9
    cot_x = 1/math.tan(x)
    area = 9/4 * int(s)**2 * cot_x
    print("Area of nonagon ≈ " + str(round(area,2)) + "²")
    delay(5)
    return main()

def Decagon():
     # area = 5/2 * s^2 * sqrt(5 + (2 * sqrt(5)))
     s = input("Enter side length: ")
     cls()
     area = 5/2 * int(s)**2 * math.sqrt(5 + (2 * math.sqrt(5)))
     print("Area of decagon ≈ " + str(round(area,2)) + "²")
     delay(5)
     return main()

def Hendecagon():
    # area = 11/4 * s^2 * cot(pi/11)
    s = input("Enter side length: ")
    cls()
    x = math.pi / 11
    cot_x = 1/math.tan(x)
    area = 11/4 * int(s)**2 * cot_x
    print("Area of hendecagon ≈ " + str(round(area,2)) + "²")
    delay(5)
    return main()

def Dodecagon():
    # area = 3 * (2 + sqrt(3)) * s^2
    s = input("Enter side length: ")
    cls()
    area = 3 * (2 + math.sqrt(3)) * int(s)**2
    print("Area of dodecagon ≈ " + str(round(area,2)) + "²")
    delay(5)
    return main()

def Triskaidecagon():
    # area = 13/4 * s^2 * cot(pi/13)
    s = input("Enter side length: ")
    cls()
    x = math.pi / 13
    cot_x = 1/math.tan(x)
    area = 13/4 * int(s)**2 * cot_x
    print("Area of triskaidecagon ≈ " + str(round(area,2)) + "²")
    delay(5)
    return main()

def Tetrakaidecagon():
    # area = 14/4 * s^2 * cot(pi/14)
    s = input("Enter side length: ")
    cls()
    x = math.pi / 14
    cot_x = 1/math.tan(x)
    area = 14/4 * int(s)**2 * cot_x
    print("Area of tetrakaidecagon ≈ " + str(round(area,2)) + "²")
    delay(5)
    return main()

def Pentadedecagon():
    # area = 15/4 * s^2 * cot(pi/15)
    s = input("Enter side length: ")
    cls()
    x = math.pi / 15
    cot_x = 1/math.tan(x)
    area = 15/4 * int(s)**2 * cot_x
    print("Area of pentadedecagon ≈ " + str(round(area,2)) + "²")
    delay(5)
    return main()

def Hexadecagon():
    # area = 4 * s^2 * cot(pi/16)
    s = input("Enter side length: ")
    cls()
    x = math.pi / 16
    cot_x = 1/math.tan(x)
    area = 4 * int(s)**2 * cot_x
    print("Area of hexadecagon ≈ " + str(round(area,2)) + "²")
    delay(5)
    return main()

def Heptadecagon():
    # area = 17/4 * s^2 * cot(pi/17)
    s = input("Enter side length: ")
    cls()
    x = math.pi / 17
    cot_x = 1/math.tan(x)
    area = 17/4 * int(s)**2 * cot_x
    print("Area of heptadecagon ≈ " + str(round(area,2)) + "²")
    delay(5)
    return main()

def Octadecagon():
    # area = 18/4 * s^2 * cot(pi/18)
    s = input("Enter side length: ")
    cls()
    x = math.pi / 18
    cot_x = 1/math.tan(x)
    area = 18/4 * int(s)**2 * cot_x
    print("Area of octadecagon ≈ " + str(round(area,2)) + "²")
    delay(5)
    return main()

def Enneadecagon():
    # area = 19/4 * s^2 * cot(pi/19)
    s = input("Enter side length: ")
    cls()
    x = math.pi / 19
    cot_x = 1/math.tan(x)
    area = 19/4 * int(s)**2 * cot_x
    print("Area of enneadecagon ≈ " + str(round(area,2)) + "²")
    delay(5)
    return main()

def Icosagon():
    # area = 5 * s^2 * (1 + sqrt(5) + sqrt(5 + (2 * sqrt(5))))
    s = input("Enter side length: ")
    cls()
    area = 5 * int(s)**2 * (1 + math.sqrt(5) + math.sqrt(5 + (2 * math.sqrt(5))))
    print("Area of icosagon ≈ " + str(round(area,2)) + "²")
    delay(5)
    return main()

def Triacontagon():
    # area = 15/2 * s^2 * cot(pi/30)
    s = input("Enter side length: ")
    cls()
    x = math.pi / 30
    cot_x = 1/math.tan(x)
    area = 15/2 * int(s)**2 * cot_x
    print("Area of triacontagon ≈ " + str(round(area,2)) + "²")
    delay(5)
    return main()

def Tetracontagon():
    # area = 10 * s^2 * cot(pi/40)
    s = input("Enter side length: ")
    cls()
    x = math.pi / 40
    cot_x = 1/math.tan(x)
    area = 10 * int(s)**2 * cot_x
    print("Area of tetracontagon ≈ " + str(round(area,2)) + "²")
    delay(5)
    return main()

def Pentacontagon():
    # area = 25/2 * s^2 * cot(pi/40)
    s = input("Enter side length: ")
    cls()
    x = math.pi / 50
    cot_x = 1/math.tan(x)
    area = 25/2 * int(s)**2 * cot_x
    print("Area of pentacontagon ≈ " + str(round(area,2)) + "²")
    delay(5)
    return main()

def Hexacontagon():
    # area = 15 * s^2 * cot(pi/60)
    s = input("Enter side length: ")
    cls()
    x = math.pi / 60
    cot_x = 1/math.tan(x)
    area = 15 * int(s)**2 * cot_x
    print("Area of hexacontagon ≈ " + str(round(area,2)) + "²")
    delay(5)
    return main()

def Heptacontagon():
    # area 35/2 * s^2 * cot(pi/70)
    s = input("Enter side length: ")
    cls()
    x = math.pi / 70
    cot_x = 1/math.tan(x)
    area = 35/2 * int(s)**2 * cot_x
    print("Area of heptacontagon ≈ " + str(round(area,2)) + "²")
    delay(5)
    return main()

def Octacontagon():
    # area 20 * s^2 * cot(pi/80)
    s = input("Enter side length: ")
    cls()
    x = math.pi / 80
    cot_x = 1/math.tan(x)
    area = 20 * int(s)**2 * cot_x
    print("Area of octacontagon ≈ " + str(round(area,2)) + "²")
    delay(5)
    return main()

def Enneacontagon():
    # area 45/2 * s^2 * cot(pi/90)
    s = input("Enter side length: ")
    cls()
    x = math.pi / 90
    cot_x = 1/math.tan(x)
    area = 45/2 * int(s)**2 * cot_x
    print("Area of enneacontagon ≈ " + str(round(area,2)) + "²")
    delay(5)
    return main()

def Hectogon():
    # area = 25 * s^2 * cot(pi/100)
    s = input("Enter side length: ")
    cls()
    x = math.pi / 100
    cot_x = 1/math.tan(x)
    area = 25 * int(s)**2 * cot_x
    print("Area of hectogon ≈ " + str(round(area,2)) + "²")
    delay(5)
    return main()

def Chiliagon():
    # area = 250 * s^2 * cot(pi/1000)
    s = input("Enter side length: ")
    cls()
    x = math.pi / 1000
    cot_x = 1/math.tan(x)
    area = 250 * int(s)**2 * cot_x
    print("Area of chiliagon ≈ " + str(round(area,2)) + "²")
    delay(5)
    return main()

def Myriagon():
    # area = 2500 * s^2 * cot(pi/10000)
    s = input("Enter side length: ")
    cls()
    x = math.pi / 10000
    cot_x = 1/math.tan(x)
    area = 2500 * int(s)**2 * cot_x
    print("Area of myriagon ≈ " + str(round(area,2)) + "²")
    delay(5)
    return main()

def select_shape_to_caluclate_area(choice):
    if choice == "3": 
        Triangle()
    elif choice == "4":
        Square()
    elif choice == "5":
        Pentagon()
    elif choice == "6":
        Hexagon()
    elif choice == "7":
        Heptagon()
    elif choice == "8":
        Octagon()
    elif choice == "9":
        Nonagon()
    elif choice == "10":
        Decagon()
    elif choice == "11": 
        Hendecagon()
    elif choice == "12": 
        Dodecagon()
    elif choice == "13":
        Triskaidecagon()
    elif choice == "14": 
        Tetrakaidecagon()
    elif choice == "15": 
        Pentadedecagon()
    elif choice == "16":
        Hexadecagon()
    elif choice == "17": 
        Heptadecagon()
    elif choice == "18": 
        Octadecagon()
    elif choice == "19": 
        Enneadecagon()
    elif choice == "20": 
        Icosagon()
    elif choice == "30": 
        Triacontagon()
    elif choice == "40": 
        Tetracontagon()
    elif choice == "50": 
        Pentacontagon()
    elif choice == "60": 
        Hexacontagon()
    elif choice == "70": 
        Heptacontagon()
    elif choice == "80": 
        Octacontagon()
    elif choice == "90": 
        Enneacontagon()
    elif choice == "100": 
        Hectogon()
    elif choice == "1000": 
        Chiliagon()
    elif choice == "10000": 
        Myriagon()
    else:
        print("Please select a valid choice.")
        return main()

def main():
    print("Calculate area of regular polygons. Choices:\n" +
    "3) Triangle\n4) Square\n5) Pentagon\n6) Hexagon\n7) Heptagon\n8) Octagon\n9) Nonagon\n10) Decagon\n11) Hendecagon\n12) Dodecagon\n13) Triskaidecagon\n14) Tetrakaidecagon\n15) Pentadedecagon\n16) Hexadecagon\n17) Heptadecagon\n18) Octadecagon\n19) Enneadecagon\n20) Icosagon\n30) Triacontagon\n40) Tetracontagon\n50) Pentacontagon\n60) Hexacontagon\n70) Heptacontagon\n80) Octacontagon\n90) Enneacontagon\n100) Hectogon\n1000) Chiliagon\n10000) Myriagon\nType \"exit\" to quit!")
    choice = input("Select choice: ")
    if choice == "exit":
        exit()
    else:
        select_shape_to_caluclate_area(choice)


if __name__ == "__main__":
    main()