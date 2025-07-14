def add(a,b): #덧셈 함수
    try: #예외 발생 가능 케이스는 a,b가 숫자가 아닌 경우임. 무효 연산식 예외
        return_value = float(a)+float(b)
        return return_value
    except:
        return "E3"

def subtract(a,b): #뺄셈 함수
    try: #예외 발생 가능 케이스는 a,b가 숫자가 아닌 경우임. 무효 연산식 예외
        return_value = float(a)-float(b)
        return return_value
    except:
        return "E3"

def multiply(a,b): #곱셈 함수
    try: #예외 발생 가능 케이스는 a,b가 숫자가 아닌 경우임. 무효 연산식 예외
        return_value = float(a)*float(b)
        return return_value
    except:
        return "E3"

def divide(a,b): #나눗셈 함수
    if (float(b)==0.0): #b가 0이면 division by zero Error
        return "E1"
    try: #예외 발생 가능 케이스는 a,b가 숫자가 아닌 경우임. 무효 연산식 예외
        return_value = float(a)/float(b)
        return return_value
    except:
        return "E3"

def operating(a,oper,b): #연산 함수
    match oper: # 연산자에 따라서 케이스 분류
        case '+': # 덧셈
            return add(a,b)
        case '-': # 뺄셈
            return subtract(a,b)
        case '*': # 곱셈
            return multiply(a,b)
        case '/': # 나눗셈
            return divide(a,b)
        case _: # 위에 것들이 모두 아니면 연산자가 무효한 케이스임, 무효 연산자 에러
            return "E2"

def split_ex(exp):
    return exp.split()

def even_is_num(lst):
    for i in range(0,len(lst),2):
        try:
            float(lst[i])
        except:
            return False
    return True

def odd_is_operator(lst):
    for i in range(1,len(lst),2):
        if not(lst[i] in ['+','-','*','/']):
            return False
    return True

def get_num_list(lst):
    return_list = []
    for i in range(0,len(lst),2):
        return_list.append(lst[i])
    return return_list

def get_operator_list(lst):
    return_list = []
    for i in range(1,len(lst),2):
        return_list.append(lst[i])
    return return_list

def func(lst_num, lst_opt):
    i = 0
    while i < len(lst_opt):
        if lst_opt[i] in ['*', '/']:
            lst_num[i] = operating(lst_num[i], lst_opt[i], lst_num[i+1])
            del lst_num[i+1]
            del lst_opt[i]
        else:
            i += 1
    while len(lst_num)>1:
        lst_num[0] = operating(lst_num[0], lst_opt[0], lst_num[1])
        del lst_num[1]
        del lst_opt[0]
    print(lst_num[0])
        
    

def main():
    expression = input("Enter expression: ") # 연산식 입력
    splitted_expression = split_ex(expression)
    
    if not(odd_is_operator(splitted_expression) and even_is_num(splitted_expression)):
        print("Invalid Input")
    else:
        num_list = get_num_list(splitted_expression)
        operator_list = get_operator_list(splitted_expression)
        func(num_list,operator_list)

if __name__ == "__main__":
    main()