import math
import numpy as np
from itertools import permutations, product
import time


size = 5
all_permutations = list(permutations(range(size)))


def evaluate(perm1,perm2):
    count = 0
    for x in range(len(perm1)):
        if perm1[x] == perm2[x]:
            count += 1
    return count


no_of_perms = len(all_permutations)
eval_matrix = np.zeros((no_of_perms, no_of_perms), dtype=int)

start =time.time()
for k in range(no_of_perms):
    if k % 10000 == 0:
        print("processing permutation %d" % k, "of %d" % no_of_perms)
    for j in range(k+1):
        eval_matrix[k][j] = evaluate(all_permutations[k], all_permutations[j]) 
        eval_matrix[j][k] = eval_matrix[k][j]
end =time.time()
print("calculation for evaluation matrix: %s" % str(end-start), "seconds")

np.save('eval_matrix.npy', eval_matrix)
#eval_matrix = np.load('eval_matrix.npy')
#print(eval_matrix)