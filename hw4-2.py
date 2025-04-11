from random import randint, choice
from string import ascii_lowercase

def gen_random_dict() -> dict:
    num_of_keys = choice(range(len(ascii_lowercase)))
    return {choice(ascii_lowercase): randint(0, 100) for i in range(num_of_keys)}

def gen_random_number_of_random_dicts() -> list[dict]:
    num_of_dicts = choice(range(2, 10))
    return [gen_random_dict() for i in range(num_of_dicts)]

random_dicts = gen_random_number_of_random_dicts()
print ("first random list", '\n',gen_random_number_of_random_dicts(),'\n')


indexing_list, tmp_dict, fin = {}, {}, {}

# indexing every dictionary to get index of it
for index, rand in enumerate(random_dicts, start =1):
    indexing_list [index] = [rand]
print ("indexing list", '\n', indexing_list,'\n')


# temp dict with all possible values
for i in random_dicts:
  for k, v in i.items():
    tmp_dict.setdefault(k, []).append(v)

print("dict with all possible values", '\n', tmp_dict,'\n')


# the final counting: if only one value for key - we paste "key: value"
# if more than one value - we get max from value and get actual index from indexing_list
for k, v in tmp_dict.items():
  if len (v) == 1:
    fin [k] = v[0]
  else:
    for index, rand in indexing_list.items():
      if k in rand[0]:
       if rand [0][k] == max(v):
        fin [k + "_"+str (index)] = max (v)
        break

# sort final result:
srt = list(fin.keys())
srt.sort()
# Sorted Dictionary
fin_sort = {i: fin[i] for i in srt}

print("sorted final results", '\n', fin_sort, '\n')