def swap(my_list, a, b):
    temp = my_list[a]
    my_list[a] = my_list[b]
    my_list[b] = temp


def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                swap(my_list, j, j+1)
    return my_list

my_love = [1, 23, 14, 16, -2, 8, 6, 9]
print("Before sorting")
print(my_love)
print("After sorting")
print(bubble_sort(my_love))


def selection_sort(my_list):
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if min_index != i:
            swap(my_list, i, min_index)
    return my_list


my_love_1 = [10, 99, -4, 22, -2, 8, 6, 9]
print("Before selection sorting")
print(my_love_1)
print("After selection sorting")
print(selection_sort(my_love_1))


def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while j >= 0 and temp < my_list[j]:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list


my_love_2 = [66, 99, -341, 25, -20, 89, 16, 29]
print("Before insertion sorting")
print(my_love_2)
print("After insertion sorting")
print(insertion_sort(my_love_2))


# def merge(list1, list2):
#     i = 0
#     j = 0
#     combined = []
#     while i < len(list1) and j < len(list2):
#         if list1[i] < list2[j]:
#             combined.append(list1[i])
#             i += 1
#         else:
#             combined.append(list2[j])
#             j += 1
#     while i < len(list1):
#         combined.append(list1[i])
#         i += 1
#     while j < len(list2):
#         combined.append(list2[j])
#         j += 1
#     return combined
#
#
# def merge_sort(mylist):
#     if len(mylist) == 1:
#         return
#     mid_index = int(len(mylist) / 2)
#     left = merge_sort(mylist[:mid_index])
#     right = merge_sort(mylist[mid_index:])
#     return merge(left, right)

def merge(list1, list2):
    i = j = 0
    combined = []
    while i < len(list1) or j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined


def merge_sort(mylist):
    if len(mylist) == 1:
        return
    mid_index = int(len(mylist) / 2)
    left = mylist[:mid_index]
    right = mylist[mid_index:]
    return merge(left, right)


my_love_3 = [66, 99, -341, 25, -20, 89, 16, 29]
print("Before merge sorting")
print(my_love_3)
print("After merge sorting")
print(insertion_sort(my_love_3))


# def pivot(mylist, pivot_index, end_index):
#     swap_index = pivot_index
#     for i in range(pivot_index+1, end_index+1):
#         if mylist[i] < mylist[pivot_index]:
#             swap_index += 1
#             swap(mylist, swap_index, i)
#     swap(mylist, pivot_index, swap_index)
#     return swap_index
#
#
# def quick_sort_helper(mylist, left, right):
#     if left < right:
#         pivot_index = pivot(mylist, left, right)
#         quick_sort_helper(mylist, left, pivot_index-1)
#         quick_sort_helper(mylist, pivot_index+1, right)
#     return mylist
#
#
# def quick_sort(mylist):
#     return quick_sort_helper(mylist, 0, len(mylist)-1)

def pivot(mylist, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if mylist[i] < mylist[pivot_index]:
            swap_index += 1
            swap(mylist, swap_index, i)
    swap(mylist, swap_index, pivot_index)
    return swap_index


def quick_sort_helper(mylist, left, right):
    if left < right:
        pivot_index = pivot(mylist, left, right)
        quick_sort_helper(mylist, left, pivot_index - 1)
        quick_sort_helper(mylist, pivot_index+1, right)
    return mylist


def quick_sort(mylist):
    return quick_sort_helper(mylist, 0, len(mylist) - 1)

my_love_4 = [66, 99, -341, 25, -20, 89, 16, 29]
print("Before quick sorting")
print(my_love_4)
print("After quick sorting")
print(insertion_sort(my_love_4))