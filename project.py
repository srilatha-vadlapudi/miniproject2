print("******* Sample Calculator *******")
print("1.Addition")
print("2.SUbtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exit")
def add(a,b):
    return "sum is",a+b
def sub(a,b):
    return "difference is",a-b
def mul(a,b):
    return "product is",a*b
def div(a,b):
    return "division  is",a/b
option=int(input("Enter Option"))
if option==5:
    print("Exit")
    
if option in[1,2,3,4,5]:
    n1=int(input("enter first number"))
    n2=int(input("enter second number"))
if option==1:
    print(add(n1,n2))
elif option==2:
    print(sub(n1,n2))
elif option==3:
    print(mul(n1,n2))
elif option==4:
    if n2!=0:
      print(div(n1,n2))
else:
    print("invalid!")
    
    


    


    


    
