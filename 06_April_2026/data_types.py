'''

1. Data types are dynamic i.e., change its data type according to the value given 
2. size of data type is also dynamic i.e., data types are not pf fixed size as in c and c++
3. data types are unbounded i.e., do not have min or max value 

dynamic = assign different values to same variable at different point of time.

'''

# 1st point example 
a = 10  
print(a)

a = "python"
print(a)

# 2nd point example 

import sys 
c = 500                         # 28
print(sys.getsizeof(c))

c = 50000000000000 * 1000000
print(sys.getsizeof(c))         # 36

c = c*c
print(sys.getsizeof(c))         # 44

#3rd point example 

c = 50000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
print(sys.getsizeof(c))         # 84
print(c)    