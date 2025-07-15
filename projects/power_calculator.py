def get_power(num,exp) -> float:
    val = 1
    if float(exp)>0:
        for i in range(int(exp)):
            val = val*float(num)
    elif float(exp) < 0:
        exp = -1 * float(exp)
        for i in range(int(exp)):
            val = val/float(num)
    else:
        val = 1
    return val

def is_num(number) -> bool:
    try: # 예외처리 구문
        float(number) # 실수형으로 형변환 시도: 성공하면 숫자. 오류나면 숫자 아님
        return True
    except:
        return False
    
def is_int(number) -> bool: # 정수 판별 함수
    if is_num(number):
        if float(number)==int(float(number)):
            return True
        else: return False
    else: return False
    
    
def main():
    number = input("Enter number: ")
    exponent = input("Enter Exponent: ")
    
    #print(is_num(number))
    #print(is_int(exponent))

    if not(is_num(number) and is_int(exponent)):
        if is_num(number) == False:
            print("Invalid number input")
        if is_int(exponent) == False:
            print("Invalid exponent input")
    else:
        print(get_power(number,exponent))
        

if __name__ == "__main__":
    main()

