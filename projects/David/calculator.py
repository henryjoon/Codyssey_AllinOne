def add(a,b) -> int:
    return a+b

def subtract(a,b) -> int:
    return a-b

def multiply(a,b) -> int:
    return a*b

def divide(a,b) -> float:
    return a/b

def is_num(a) -> bool:
    try:
        float(a)
        return True
    except:
        return False

def which_opt(a):
    if a in ['+','-','*','x','X','/']:
        if a == '+':
            return True, "add"
        elif a == '-':
            return True, "subtract"
        elif a == '/':
            return True, "divide"
        else:
            return True, "multiply"
    else:
        return False, "not_operator"


def main():
    num1 = input("input num1: ")
    operator = input("input operator: ")
    num2 = input("input num2: ")
    
    is_num_num1 = is_num(num1)
    is_num_num2 = is_num(num2)
    is_operator, which_operator = which_opt(operator)
    
    if is_num_num1 and is_num_num2 and is_operator:
        num1 = int(num1)
        num2 = int(num2)
        
        match which_operator:
            case "add":
                print("Result:", add(num1, num2))
            case "subtract":
                print("Result:", subtract(num1, num2))
            case "divide":
                if num2 != 0:
                    print("Result:", divide(num1, num2))
                else:
                    print("! Error: division by zero")
            case "multiply":
                print("Result:", multiply(num1, num2))
        
    else:
        print("! Invalid Input")
        if not is_num_num1:
            print("! num1 is not number")
        if not is_num_num2:
            print("! num2 is not number")
        if not is_operator:
            print("! operator you input is not an operator")

if __name__ == "__main__":
    main()