num_set = {1, 2, 3, 4, 5, 6}
print(num_set)

string_set = {"Nicholas", "Michelle", "John", "Mercy"}
print(string_set)

num_set = set([1, 6, 2, 3, 6, 4, 5, 6])
print(num_set)
print(2 in num_set)
print(7 in num_set)

months_a = set(["Jan", "Feb", "March", "Apr", "May", "June"])
months_b = set(["July", "Aug", "Sep", "Oct", "Nov", "Dec"])
print(months_a.union(months_b))

x = {1, 2, 3}
y = {4, 3, 6}
z = {7, 4, 9}
print(x | y | z)

x = {1, 2, 3}
y = {4, 3, 6}
print(x & y)

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
diff_set = set_a.difference(set_b)
print(diff_set)

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(set_a ^ set_b)