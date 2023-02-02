# Create a quadratic.py program that asks the user for three numbers (a, b, c) and calculates the two roots using the quadratic formula

a=int(input("Enter the value for a:"))
b=int(input("Enter the value for b:"))
c=int(input("Enter the value for c:"))
root1 = (-b+(b*b - 4*a*c)**0.5) / (2*a)
root2 = (-b-(b*b - 4*a*c)**0.5) / (2*a)
print(root1)
print(root2)