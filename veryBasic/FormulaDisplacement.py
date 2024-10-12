v = int(input("Enter final velocity: "))
u = int(input("Enter initial velocity: "))
a = int(input("Enter acceleration: "))

displacement = (v**2 - u**2)*1/(2*a)
print("Displacement is: ", displacement)