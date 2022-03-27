#permutations
#combinations
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement


for item in permutations('ABC', 2):
    print(''.join(item))

print()

# combinations without repetitive elements
for item in combinations('ABC', 2):
    print(''.join(item))

print()

# combinations with repetitive elements
for item in combinations_with_replacement('ABC', 2):
    print(''.join(item))