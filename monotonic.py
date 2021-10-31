from random import randint
n = int(input())
nums = [randint(1, n) for i in range(n)]
def is_monotonic(nums):
    res= False
    dec=0
    inc=0
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            dec += 1
        elif nums[i] < nums[i + 1]:
            inc += 1
        if dec == 0:
            res = True
        elif inc == 0:
            res = True
        return(res)
print(nums)
print(is_monotonic(nums))


