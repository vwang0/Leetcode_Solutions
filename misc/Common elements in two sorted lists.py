/*
Common elements in two sorted lists with duplicates (return all duplicates if exists)
*/
a = [1, 1, 2, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for i in a:
    if i in b and i not in c:
        c.append([i])
print(c)

def common_member(a, b): 
    a_set = set(a) 
    b_set = set(b) 
    if (a_set & b_set): 
        return a_set & b_set)
    else: 
        return []