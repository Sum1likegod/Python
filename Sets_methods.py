set_1 = {"item1", "item2", 12, 90.987, 213,829}
set_2 = {"item1", "item2", "item3", 9084, 213, 12,829}

# print(set_1.union(set_2))
# # set_1.update(set_2)
# print(set_1)

# # print(set_1.intersection(set_2))
# # set_1.intersection_update(set_2)
# print(set_1)


print(set_1.symmetric_difference(set_2))
set_2.symmetric_difference_update(set_1)
print(set_2)
print(set_1)


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul","jbp"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities2.issubset(cities3))

l_1 = [1, 213, 13 ,435 , "hey"]
cities2.update(l_1)
print(cities2)
print(type(cities2))


cities2.clear()
print(cities2)
