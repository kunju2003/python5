s={1,2,3,4,5,6}
s2={1,2,3,7}
print(s.difference(s2))
print(s.intersection(s2))
print(s.isdisjoint(s2))
print(s2.issubset(s))
print(s.issuperset(s2))
print(s.union(s2))
print(s.symmetric_difference(s2))
print(s.symmetric_difference_update(s2))
print(s.intersection_update(s2))
print(s.difference_update(s2))