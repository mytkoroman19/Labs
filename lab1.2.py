def find_kth_largest(nums, k):
    if not (1 <= k <= len(nums)):
        raise ValueError("k повинен бути в межах від 1 до довжини нашого масиву.")
    
    
    data = [(val, idx) for idx, val in enumerate(nums)]
    
    def quickselect(items, k_target):
        
        pivot_val, pivot_idx = items[-1]
        
      
        left = [x for x in items if x[0] > pivot_val]   
        middle = [x for x in items if x[0] == pivot_val] 
        right = [x for x in items if x[0] < pivot_val]  
        
        L = len(left)
        M = len(middle)
        
        if k_target <= L:
            return quickselect(left, k_target)
        elif k_target <= L + M:

            return middle[0]
        else:
            return quickselect(right, k_target - L - M)


    value, original_index = quickselect(data, k)
    return value, original_index

if __name__ == "__main__":
    nums = [4, 10, 5, 12, 3, 17, 1]
    k_value = 2
    
    value, position = find_kth_largest(nums, k_value)

    print(f"Масив: {nums}")
    print(f"{k_value}-й найбільший елемент: {value}")
    print(f"Його позиція в оригінальному масиві: {position}")