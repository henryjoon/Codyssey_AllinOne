def swap(a,b):
    return b,a

def get_min(lst):
    min_val = float(lst[0])
    min_index = 0
    for i in range(len(lst)):
        if float(lst[i]) < float(min_val):
            min_val = lst[i]
            min_index = i
    return float(min_val), min_index

def bubble_sorting(lst):
    while True:
        sorted_sum = 0
        repeat_time = len(lst)-1
        for i in range(repeat_time):
            if lst[i]>lst[i+1]:
                lst[i], lst[i+1] = swap(lst[i],lst[i+1])
                sorted_sum += 1
                print("    -->", lst, "changed")
            else:
                print("    -->", lst, "not changed")
        print("  ------------------")
        if sorted_sum == 0:
            return lst

def Selection_sorting(lst):
    repeat_time = len(lst) - 1
    for i in range(repeat_time):
        min_num, min_num_index = get_min(lst[i:])
        lst[i],lst[min_num_index] = swap(lst[i],lst[min_num_index])
        print("    -->", lst)
    return lst
        
    

def Insertion_sorting(lst):
    repeat_time = len(lst) - 1
    return_list = [lst[0]]
    for i in range(repeat_time):
        for j in range(len(return_list)):
            if lst[i+1] < return_list[j]:
                index = j
                break
        lst[i],lst[index] = swap(lst[i],lst[index])
        print("    -->", return_list)
    return return_list

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
    numbers = input("input numbers you want to sort:")
    numbers_list = to_num_list(numbers.split())
    print("Numbers you input:", numbers_list)
    print("------------------")
    
    print("  1. Bubble Sorting")
    print("  After bubble_sort:", bubble_sorting(numbers_list))
    print("------------------")
    
    print("  2. Selection Sorting")
    print("After selection_sort:", Selection_sorting(numbers_list))
    print("------------------")
    
    print("  3. Insertion Sorting")
    print("After selection_sort:", Insertion_sorting(numbers_list))
    print("------------------")

if __name__ == "__main__":
    main()