#1
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

si = (p * r * t) / 100
print("Simple Interest =", si)

#2
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Maximum number is:", a)
else:
    print("Maximum number is:", b)

#3
for i in range(1, 6):
    print(i)

#4
s = input("Enter a string: ")
print("Length of string =", len(s))

#5
s = input("Enter a string: ")
print("First character =", s[0])

#6
s = input("Enter a string: ")
print("Last character =", s[-1])

#7
print("Welcome to Python Programming")

#8
n = int(input("Enter a number: "))

if n > 0:
    print("Positive number")
elif n < 0:
    print("Negative number")
else:
    print("Zero")

#9
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

sum = a + b + c
print("Sum =", sum)

#10
n = int(input("Enter a number: "))
square = n * n
print("Square =", square)
