

def twosum(nums,target):
    listIndexes = [] 

    for index1 in range(len(nums)):
        for index2 in range(len(nums)):
            if index1 == index2:
                pass
            else:
                if nums[index1] + nums[index2] == target:
                    listIndexes.append(index1)
    return listIndexes



print(twosum([4,2,55,78],6))