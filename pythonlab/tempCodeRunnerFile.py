nums = [3 , 4, 5, 6, 7]
largest = nums[0]
smallest = nums[0]

for num in nums:
    if num > largest :
        largest = nums
if num < smallest:
        smallest = nums

        print("largest:", largest)
        print("smallest:", smallest)