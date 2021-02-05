def factorial (n):
for i in range (n):
    fac = fac*(i+1)
return fac 
pass

 number = int (input("Enter then number"))

print (factorial (number))