def bubble_sort(l):
    for i in range(0, len(l) - 1):
        for j in range(0, len(l) - 1 - i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    
    return l


list = ['a', 'c', 'd', 'f', 'e', 'b']
print(bubble_sort(list))