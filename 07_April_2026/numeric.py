''' int '''

a = 5
print(type(a))

a = -5
print(type(a))


# can store both +ve and -ve numbers but not fractions 


''' float '''

c = 5.5 
print(type(c))

c = 3.1341212212
print(type(c))

# can store integers with decimal points 
# can store exponential values 

e = 1e5  #100000.0
print(type(e))

e = 1e-3   #0.001
print(type(e))



''' Complex '''

# of form x+yi, not x+iy
# can only use letter j 

c = 3+5j
print(type(c))

print(c.real)
print(c.imag)


