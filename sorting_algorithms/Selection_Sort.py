def selection_sort(l):
    for i in range(len(l)):
        min_value = i
        for j in range(i + 1, len(l)):
            if l[j] < l[min_value]:
                min_value = j
        l[i], l[min_value] = l[min_value], l[i]


list = [0, 1, 7, 9, 6, 3, 4, 2, 5, 8]
selection_sort(list)
print(list)