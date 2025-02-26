import collections
from collections import defaultdict
from random import randint, choice
from string import ascii_lowercase

# creating random list according task
random = [{choice(ascii_lowercase): randint(0, 100) for i in range(len(ascii_lowercase))} for j in range(randint(2, 10))]

print ("first random list", '\n',random,'\n')

rand12 = {}

# indexing every dictionary to get index of it
for index, rand in enumerate(random, start =1):
    rand12 [index] = [rand]
print ("indexing list", '\n', rand12,'\n')

tmp_dict, fin = {}, {}

# temp dict with all possible values
for dictionary in random:
  for k, v in dictionary.items():
    tmp_dict.setdefault(k, []).append(v)

print("dict with all possible values", '\n', tmp_dict,'\n')


# the final counting: if only one value for key - we paste "key: value"
# if more than one value - we get max from value and get actual index from rand12
for k, v in tmp_dict.items():
  if len (v) == 1:
    fin [k] = v[0]
  else:
    for index, rand in rand12.items():
      if k in rand[0]:
       if rand [0][k] == max(v):
        fin [k + "_"+str (index)] = max (v)
        break

print('\n', "results", '\n', fin,'\n')



print ("for checking separate dictionaries:")

#checking
for index, rand in enumerate(random, start =1):
  print (index, rand)

# sort final result:
srt = list(fin.keys())
srt.sort()
# Sorted Dictionary
fin_sort = {i: fin[i] for i in srt}
print('\n',"sorted final results", '\n', fin_sort, '\n')
