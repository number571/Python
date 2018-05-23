# Public
p = 3001 # Простое число
g = 3    # Натуральное число

if g**(p-1)%p != 1: 
    raise SystemExit

# Private
a = 41 # Натуральное число Alice
b = 12 # Натуральное число Bob
# e = 31 # Натуральное число Eve

# Public
A = g**a%p # Alice
B = g**b%p # Bob
# E = g**e%p # Eve
print(A, B) # , E

# Private
kA = B**a%p # Key
kB = A**b%p # Key
# kE = A**e%p # Key
print(kA, kB) # , kE

# Eve have:
# p, g, A, B
