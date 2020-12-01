
input = open('input.txt','r')

nums = []

for num in input:
    nums.append(int(num))

def find_triplet():
    for number in nums:
        possible_second_numbers = [num for num in nums if num < (2020 - number) ]
        for num in possible_second_numbers:
            if 2020 - num - number in nums:
                print(str(number))
                print(str(num))
                print(str(2020 - number - num))
                return

find_triplet()
