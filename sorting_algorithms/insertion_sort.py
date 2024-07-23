def insertion_sort(list):
    """This function uses swaps for the insertion sort"""
    for i in range(1, len(list)):
        j = i - 1
        while list[j] > list[j + 1] and j >= 0:
            list[j], list[j + 1] = list[j+1], list[j]
            j -= 1


def shifting_insertion_sort(l):
    for i in range(1, len(l)):
        currNum = l[i]
        for j in range(i-1, 0, -1):
            if l[j] > currNum:
                l[j+1] = l[j]
            else:
                l[j+1] = currNum
                break
