def add(a,b):
    return int(a)+int(b)

def subtract(a,b):
    return int(a)-int(b)

def multiply(a,b):
    return int(a)*int(b)

def divide(a,b):
    try:
        return int(a)/int(b)
    except:
        return "E1"

def operating(a,oper,b):
    match oper:
        case '+':
            return add(a,b)
        case '-':
            return subtract(a,b)
        case '*':
            return multiply(a,b)
        case '/':
            return divide(a,b)
        case _:
            return "E2"

def main():
    num1 = input("num1: ")
    opt = input("operator: ")
    num2 = input("num2: ")

    result = operating(num1,opt,num2)

    if (result == "E1"):
        print("Error:Division by zero")
    elif (result == "E2"):
        print("Invalid operator")
    else:
        print("Result:", result)

if __name__ == "__main__":
    main()
        