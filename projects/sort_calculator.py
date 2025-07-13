def sorting(lst):
    return_list = [] #새로운 리스트
    for val in lst: #lst에 있는 값 모두 순회
        inserted = False #기본적으로 '삽입됨'을 의미하는 변수 inserted의 값을 False로 설정함
        for i in range(len(return_list)): #return_list 길이만큼 반복, 처음엔 0이니까 스킵
            if val < return_list[i]:
                return_list.insert(i, val)
                inserted = True
                break
        if not inserted: #위에서 걸러지지 않았다면 inserted=False이고 val 값이 가장 큰 값이라는 것임.
            return_list.append(val)
    return return_list

    
def is_all_num(lst):
    for val in lst:
        try:
            float(val)
        except:
            return False
    return True

def is_not_empty(lst):
    if len(lst) == 0:
        return False
    else:
        return True

def to_num_list(lst):
    return_list=[]
    for val in lst:
        return_list.append(float(val))
    return return_list

def split_values(val):
    return_list = val.split()
    return return_list


input_value = input("Input numbers.")
input_value_list = to_num_list(split_values(input_value))

print(sorting(input_value_list))