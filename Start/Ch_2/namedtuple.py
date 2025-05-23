# Demonstrate the usage of namdtuple objects

import collections


# TODO: create a Point namedtuple
Point = collections.namedtuple('Point', ['x', 'y'])

p1 = Point(10, 20)
p2 = Point(30, 40)
print(f"p1: {p1}, p2: {p2}")
print(f"p1.x: {p1.x}, p1.y: {p1.y}")
print(f"p2.x: {p2.x}, p2.y: {p2.y}")

# TODO: use _replace to create a new instance
p1 = p1._replace(x=100)
print(f"p1: {p1}")