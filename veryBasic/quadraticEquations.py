import math

a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
c = int(input("Enter c value: "))

root1 = (-b + math.sqrt(b**2- 4*a *c))/(2*a)
root2 = (-b - math.sqrt(b**2 - 4*a *c))/(2*a)

print("root1 = ", root1)
print("root2 = ", root2)