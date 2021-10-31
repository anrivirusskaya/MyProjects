def ind_missing_nums(nums):
    n = max(nums)
    nums1 = list(range(1,n+1))
    m = []
    for i in nums1:
        if i not in nums:
            m.append(i)
    print("Недостающие элементы списка:",m)


