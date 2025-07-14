########## 연산 기능 #################################################

def add(a,b): #덧셈 함수

    return_value = float(a)+float(b)
    return return_value
    
def subtract(a,b): #뺄셈 함수
    return_value = float(a)-float(b)
    return return_value

def multiply(a,b): #곱셈 함수
    return_value = float(a)*float(b)
    return return_value

def divide(a,b): #나눗셈 함수
    return_value = float(a)/float(b)
    return return_value
    
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

##################################################################


########## 입력 식 가공 ############################################
# 입력 식 쪼개기
def split_ex(exp):
    return exp.split()

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
##################################################################


############ 오류 확인 ############################################
    #### 입력 식 판단 - 숫자 연산자 숫자 연산자 ... 이렇게 입력되었나 확인 #####
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
    ################################################################
    
    #### 0으로 나눈 적이 있나 확인 ######################################
def No_div_0_Error(lst_num, lst_opt):
    div_index = []
    for i in range(len(lst_opt)):
        if lst_opt[i] == '/':
            div_index.append(i)
    for j in range(len(div_index)):
        if float(lst_num[div_index[j]+1]) == 0.0:
            return False
    return True
    ################################################################
####################################################################


############ 곱셈과 나눗셈 먼저 계산하게 해주는 함수 ##########################
def priority_operating(lst_num, lst_opt):
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
####################################################################


############ 메인 함수 ###############################################
def main():
    expression = input("Enter expression: ") # 연산식 입력
    splitted_expression = split_ex(expression)
    num_list = get_num_list(splitted_expression)
    operator_list = get_operator_list(splitted_expression)
    
    if not(odd_is_operator(splitted_expression) and even_is_num(splitted_expression)):
        print("Invalid Input")
    elif not(No_div_0_Error(num_list,operator_list)):
        print("Error: Division by zero.")
    else:
        priority_operating(num_list,operator_list)
####################################################################


# 직접 실행되면 메인함수 호출
if __name__ == "__main__":
    main()
    
