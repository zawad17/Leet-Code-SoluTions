def pair_two_sum(nums, target):
    left = 0
    right = len(nums) - 1
    while (left < right) :
        current_value = nums[left] + nums[right]

        if current_value == target:
            return [nums[left], nums[right]]
        elif nums[left] + nums[right] < target :
            left +=1
        else:
            right -=1
    return []

nums = [1, 2, 4, 7, 11, 15]
target = 15
result = pair_two_sum(nums, target)
if result:
    print("Index: ",(nums.index(result[0]), nums.index(result[1])))
    print("Pair found:", result)
    
        
  
