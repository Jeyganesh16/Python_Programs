def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b != 0:
        return a/b
    else:
        return "Error:Division by zero"

print("Simple Calculator")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
choice=int(input("Enter your choice 1 to 4"))
num1=float(input("Enter number 1"))
num2=float(input("Enter number 2"))
match choice:
    case 1:
        print("Result:",add(num1,num2))
    case 2:
        print("Result:",sub(num1,num2))
    case 3:
        print("Result:",mul(num1,num2))
    case 4:
        print("Result:",div(num1,num2))
    case _:
        print("Invalid option:Please select 1 to 4")
