import numpy as np
from statistics import mean

# creating random list, using "random" function
lst = [np.random.randint(0, 1000) for _ in range (100)]
print('random list:', lst)

#instead range we can use "size" value from random:
#lst = np.random.randint(0, 1000, 100)
#but in this case all results for other counting will be displayed in such way:
# even: [np.int32(324), np.int32(118), np.int32(668), ... ]



# sort list from min to max(without using sort()). I got this method from Google

for run in range(len(lst) - 1):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
print('\nsorted list:', lst)

#Declare arrays/lists for even and odd
even = []
odd = []

#devision each value from the list to 2 and using  % (modulo) operator we check if the value is even or odd
#after checking we gather the values to the relevant list
for k in lst:
    if k % 2 == 0:
        even.append(k)
    else:
        odd.append(k)

#using statistic operator "mean()" we get the average for each list
#other case - we sum elements from the lists and devision to the lenth of list:
# avg_even = sum(even) / len(even) if even else 0
avg_even = mean(even) if len(even) > 0 else "don't have even values"
avg_odd = mean(odd) if len(odd) > 0 else "don't have odd values"

print('\neven:', even, '\navg even:', avg_even)
print('\nodd:', odd, '\navg odd:',avg_odd)