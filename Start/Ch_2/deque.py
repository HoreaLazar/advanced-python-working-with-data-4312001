# deque objects are like double-ended queues

import collections
import string


# TODO: initialize a deque with lowercase letters
d = collections.deque(string.ascii_lowercase)

# TODO: deques support the len() function
print(f"Item Count: {len(d)}") 

# TODO: deques can be iterated over
for item in d:
    print(item.upper())

# TODO: manipulate items from either end
d.pop() # remove the last item
d.popleft() # remove the first item
d.append(2) # add to the end of the deque
d.appendleft(1) # add to the front of the deque
print(d)  # access the first item in the deque


# TODO: use an index to get a particular item
print(d)
d.rotate(1)
print(d)