side = int(input("Enter the length of a side of the square: "))

def area_of_square(s):
    return s * s

def perimeter_of_square(s):
    return 4 * s

print(f"Area of the square: {area_of_square(side)}")
print(f"Perimeter of the square: {perimeter_of_square(side)}")