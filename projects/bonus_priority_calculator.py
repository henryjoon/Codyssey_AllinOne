########## 연산 기능 #################################################

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

def operating(exp):
    num_stack = []
    postfix_list = exp.split()
    operator = ['+','-','*','+']
    #print(postfix_list)
    
    for val in postfix_list:
        if is_num(val):
            num_stack.append(val)
        elif val in operator:
            num2 = num_stack.pop()
            num1 = num_stack.pop()
            match val:
                case '+':
                    num_stack.append(add(float(num1),float(num2)))
                case '-':
                    num_stack.append(subtract(float(num1),float(num2)))
                case '*':
                    num_stack.append(multiply(float(num1),float(num2)))
                case '/':
                    num_stack.append(divide(float(num1),float(num2)))
        
    print(num_stack[0])
    

def to_postfix(lst):
    stack_list = []
    priority1 = ['*', '/']
    priority2 = ['+', '-']
    expression = ""
    next_of_bracket = False
    for val in lst:
        if is_num(val):
            expression = expression + val + " "
        else:
            if not stack_list or val == '(':
                stack_list.append(val)
                if val == '(':
                    next_of_bracket = True
                else:
                    next_of_bracket = False
            elif next_of_bracket:
                stack_list.append(val)
                if val == '(':
                    next_of_bracket = True
                else:
                    next_of_bracket = False
            else:
                if val in priority1:
                    if stack_list[len(stack_list)-1] in priority1:
                        expression = expression + stack_list.pop() + " "
                        stack_list.append(val)
                    elif stack_list[len(stack_list)-1] in priority2:
                        stack_list.append(val)
                elif val in priority2:
                    expression = expression + stack_list.pop() + " "
                    stack_list.append(val)
                elif val == ')':
                    while True:
                        opt = stack_list.pop()
                        if opt == '(':
                            break
                        else:
                            expression = expression + opt + " "
    while len(stack_list) != 0:
        expression = expression + stack_list.pop() + " "
    return expression

##################################################################


########## 입력 식 가공 ############################################

def split_ex(exp): # 입력 식 쪼개기
    del_space_exp = ''
    for txt in exp:
        if txt != ' ':
            del_space_exp += txt
    
    return_list = []
    element = ''
    
    for val in del_space_exp:
        if val in ['+','-','*','/','(',')']:
            if element != '':
                return_list.append(element)
                element = ''
            return_list.append(val)
        elif is_num(val):
            element += val
        else:
            print("Invalid Input")
    return_list.append(element)
    return return_list

##################################################################

########## 오류 발생 확인 ###########################################


####################################################################

########## 조건 판단 ###########################################

def is_num(a) -> bool:
    try:
        float(a)
        return True
    except:
        return False

############ 메인 함수 ###############################################

def main():
    expression = input("Enter expression: ") # 연산식 입력
    splitted_expression = split_ex(expression)
    postfix = to_postfix(splitted_expression)
    #print(postfix)
    operating(postfix)
        
        
####################################################################


# 직접 실행되면 메인함수 호출
if __name__ == "__main__":
    main()
    
