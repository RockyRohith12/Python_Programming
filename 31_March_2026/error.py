'''
2 types of errors = 

1. Syntax error 
2. Runtime error 

'''


#1. Syntax error examples 

print("Hello World"      #SyntaxError: '(' was never closed
prin("Hello world")       #NameError: name 'prin' is not defined. Did you mean: 'print'?


#2. Runtime error examples 

a=5
b=0

print(a/b)  #ZeroDivisionError: division by zero

#if any other line is present after this runtime error line then it also doesnt get printed

