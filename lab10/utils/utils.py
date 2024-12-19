import random

def quick_sort(nums, key=lambda x: x, comp=lambda x, y: x < y):
    if len(nums) <= 1:
        return nums
    pivot = key(nums[random.randint(0, len(nums) - 1)])
    left = [x for x in nums if comp(key(x), pivot)]
    middle = [x for x in nums if key(x) == pivot]
    right = [x for x in nums if comp(pivot, key(x))]
    return quick_sort(left, key, comp) + middle + quick_sort(right, key, comp)

def filter(l, key=lambda x: x):
    return [x for x in l if key(x)]

def __backtack(start:int,current_group:list,seen:set,k:int,result:list,source:list):
    if len(current_group) == k:
        result.append(current_group.copy())
        return
    
    for i in range(start,len(source)):
        if i in seen:
            continue
        current_group.append(source[i])
        seen.add(i)
        __backtack(i,current_group,seen,k,result,source)
        seen.remove(i)
        current_group.pop()

def form_k_groups(k:int,source:list):
    result = []
    __backtack(0,[],set(),k,result,source)
    return result