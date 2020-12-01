
input = open('input.txt','r')

nums = input.readlines()

print(nums)

for num in nums:
    if str(2020 - int(num)) +'\n' in nums:
        print(int(num) * (2020 - int(num)))
