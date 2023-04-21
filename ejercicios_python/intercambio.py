# A = input("ingrese valor A")
# B = input("ingrese valor B")

# I = B
# B = A
# B = I

# print(B, A)

# forma de hacerlo 2
A = input("ingrese valor A")
B = input("ingrese valor B")

A, B = B, A

print(A, B)
