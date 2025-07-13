def print_power(num,exp):
    val = 1
    for i in range(int(exp)):
        val = val * float(num)
    print(val)

def is_num(obj):
    try:
        float(obj)
        return True
    except:
        print("Invalid number input.")
        return False
    
def is_int(obj):
    for i in range(len(obj)):
        if not('0' <= obj[i] <= '9'):
            print("Invalid exponent input")
            return False
    return True

number = input("Enter number: ")
exponent = input("Enter Exponent: ")

if (is_num(number) and is_int(exponent)):
    print_power(number,exponent)