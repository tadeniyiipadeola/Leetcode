

def twosum(nums, target):
    required = {}
    for i in range(len(nums)):
        if target - nums[i] in required:
            return[required[target - nums[i]], i]
        else:
            required[nums[i]] =i




input_list = [2,8,12,15]
target = 20
print(twosum(input_list, target))


