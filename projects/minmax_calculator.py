def get_max(lst):
    max_val = float(lst[0])
    for i in range(len(lst)):
        if float(lst[i]) > float(max_val):
            max_val = lst[i]
    return float(max_val)

def get_min(lst):
    min_val = float(lst[0])
    for i in range(len(lst)):
        if float(lst[i]) < float(min_val):
            min_val = lst[i]
    return float(min_val)

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
        

def split_values(val):
    return_list = val.split()
    return return_list
    
input_value = input("Input numbers.")
input_value_list = split_values(input_value)

if is_all_num(input_value_list) and is_not_empty(input_value_list):
    print(get_max(input_value_list))
    print(get_min(input_value_list))

else:
    print("Invalid inputs")