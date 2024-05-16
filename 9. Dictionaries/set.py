set1 = {1,2,3,4}
set2 = {4,5,6,7}

# Add
set1.add(5)
print(set1)

# Remove
set1.remove(5)
print(set1)

# Union
union_set = set1.union(set2)
print(union_set)

# Intersection
intersection_set = set2.intersection(set1)
print(intersection_set)

# difference
diff_set = set1.difference(set2)
print(diff_set)