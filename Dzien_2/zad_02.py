
nums=[]
for i in range(10):
    nums.append(int(input(f"Podaj liczbe {i+1}: ")))

if len(nums)>0:
    min=nums[0]
    max=nums[0]
    for i in nums:
        if i>max:
            max=i
        if i<min:
            min=i

    print(f"Min: {min}, Max: {max}")