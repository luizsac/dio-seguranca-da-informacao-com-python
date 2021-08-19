import itertools
import string

result = itertools.permutations(string.ascii_letters + string.digits, 3)

for i in result:
    print(''.join(i))
