# YOUR CODE HERE
n = int(input())
lst1 = []
lst2 = [] 

for i in range (n):
    a = int(input())
    lst1.append(a)

for i in range (n):
    b = int(input())
    lst2.append(b)

def summation(lst1,lst2):
    lst3 = []
    for i in range(len(lst1)):
        lst3.append(lst1[i] + lst2[i])
    return lst3

def find_min_max(lst3):
    min_value = min(lst3)
    max_value = max(lst3)
    return (min_value , max_value)

lst3 = summation(lst1 , lst2)
print (lst3)

min_max = find_min_max(lst3)
print (min_max)
