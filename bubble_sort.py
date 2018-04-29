import random
global ten_thousand_list
ten_thousand_list = []
for i in range(10001):
    num = random.randint(-10000,10000)
    ten_thousand_list.append(num)

#working
# avg run time 10.811s
def bubble_sort(arr):
    for x in range(len(arr) - 1):
        for y in range(0, len(arr) - 1 - x):
            if arr[y] > arr[y + 1]:
                arr[y], arr[y + 1] = arr[y + 1], arr[y]

    print arr
bubble_sort(ten_thousand_list)



#working
# avg run time 15.215s
def bubble_sort2(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                swapped = True
    print arr
bubble_sort2(ten_thousand_list)
