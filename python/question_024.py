from itertools import permutations

print("".join(map(str, sorted(permutations([0,1,2,3,4,5,6,7,8,9]))[999999])))
