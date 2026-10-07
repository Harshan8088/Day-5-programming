def add(a,b):
    return a+b
def subtract(a,b):
    return a-b

def multiplay(a,b):
    return a*b

def vivide(a,b):
    return a/b

while True:
    print("**Simple calculator**")
    print("1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division\n 5.Exit")
   

    choice=int(input("enter youe choice:"))
    if choice in {1,2,3,4}:
        a=int(input("enter first number:"))
        b=int(input("enter second number:"))
    if choice==1:
        print("Addition:",add(a,b))
    elif choice==2:
        print("Subtraction:",subtract(a,b))
    elif choice==3:
        print("Multiplication:",multiplay(a,b))
    elif choice==4:
        print("Division:",vivide(a,b))
    elif choice==5:
        print("Exiting the calculator...")
        break
    else:
        print("invalid choice")