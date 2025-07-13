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
        case 0: # 연산식이 무효할 때 연산자 값을 0으로 세팅하게 해 둠,
            return "E3"
        case _: # 위에 것들이 모두 아니면 연산자가 무효한 케이스임, 무효 연산자 에러
            return "E2"
        
def NumOpNum(exp): # 숫자, 연산자, 숫자 이렇게 3개로 쪼개는 함수
    try:
        a,b,c = exp.split() # 공백 기준으로 나눠라
        return a,b,c
    except: # 안나눠지면 띄어쓰기 안했거나 항 개수가 3개 이상인 거임
        return 1,0,1
    

expression = input("Enter expression: ") # 연산식 입력
num1,opt,num2 = NumOpNum(expression) # 연산식을 숫자, 연산자, 숫자로 바꿔

result = operating(num1,opt,num2)

if (result == "E1"):
    print("Error:Division by zero")
elif (result == "E2"):
    print("Invalid operator")
elif (result == "E3"):
    print("Invalid expression")
else:
    print("Result:", result)