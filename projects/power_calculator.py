def print_power(num,exp):
    val = 1
    for i in range(int(exp)):
        val = val * float(num)
    print(val)

def is_num(obj):
    try: # 예외처리 구문
        float(obj) # 실수형으로 형변환 시도: 성공하면 숫자. 오류나면 숫자 아님
        return True
    except:
        print("Invalid number input.")
        return False
    
def is_int(obj): # 정수 판별 함수
    for i in range(len(obj)): 
        if not('0' <= obj[i] <= '9'):
            print("Invalid exponent input")
            return False
    return True

def main():
    number = input("Enter number: ")
    exponent = input("Enter Exponent: ")

    if (is_num(number) and is_int(exponent)):
        print_power(number,exponent)    

main()