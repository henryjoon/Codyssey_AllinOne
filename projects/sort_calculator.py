def get_min_index(lst):
    min_index = 0
    for i in range(1, len(lst)):
        if float(lst[i]) < float(lst[min_index]):
            min_index = i
    return min_index

def bubble_sorting(lst):
    while True:
        sorted_sum = 0
        repeat_time = len(lst)-1
        for i in range(repeat_time):
            if lst[i]>lst[i+1]:
                lst[i], lst[i+1] = lst[i+1],lst[i]
                sorted_sum += 1
                print("    -->", lst, "changed")
            else:
                print("    -->", lst, "not changed")
        print("  ------------------")
        if sorted_sum == 0:
            print("    Not changed. Quit sorting")
            return lst

def Selection_sorting(lst):
    repeat_time = len(lst) - 1
    for i in range(repeat_time):
        min_num_index = get_min_index(lst[i:])+i
        lst[i],lst[min_num_index] = lst[min_num_index],lst[i]
        print("    -->", lst)
    return lst

def Insertion_sorting(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        for j in range(i): 
            if lst[j] > key:
                lst.insert(j, key)  
                del lst[i+1]         
                break
        print("    -->", lst)
    return lst

    

def is_num(a):
    try:
        float(a)
        return True
    except:
        return False
    
def to_num_list(lst):
    for i in range(len(lst)):
        lst[i] = float(lst[i])
    return lst

def main():
    numbers = input("input numbers you want to sort\n>> ")
    false_sum = 0
    numbers_split = numbers.split()
    for val in numbers_split:
        if not is_num(val):
            false_sum += 1
    
    if false_sum != 0:
        print("Invalid inputs.")
    
    elif not numbers_split:
        print("No Inputs.")
    
    else:   
        numbers_list = to_num_list(numbers_split)
        print("Numbers you input:", numbers_list)
        method = input("1. Bubble sorting, 2. Selection Sorting, 3. Insertion Sorting\n>> ")
        print("------------------")
    
        match method:
            case '1':
                print("  1. Bubble Sorting")
                print("\n  After bubble_sort:", "  ".join(str(val) for val in bubble_sorting(numbers_list)))
                print("------------------")
    
            case '2':
                print("  2. Selection Sorting")
                print("\n  After selection_sort:", "  ".join(str(val) for val in Selection_sorting(numbers_list)))
                print("------------------")
            
            case '3':
                print("  3. Insertion Sorting")
                print("\n  After insertion_sort:", "  ".join(str(val) for val in Insertion_sorting(numbers_list)))
                print("------------------")
            
            case _:
                print("input number of method")
            

if __name__ == "__main__":
    main()