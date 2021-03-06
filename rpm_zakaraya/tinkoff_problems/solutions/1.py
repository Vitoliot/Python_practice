import copy
numbs = [int(input( "число "))  for i in range(int(input()))]
numb_of_choices = int(input())
numbs_pot = copy.deepcopy(numbs)


def min_sort(arr, arr_pot):
    for i in range(len(arr_pot)):
        arr_pot[i] = 10**len(str(arr_pot[i])) - arr_pot[i]
    for j in range(1, len(arr)):
        for i in range(1, (len(arr))):
            if arr_pot[i - 1] < arr_pot[i]:
                swap = arr_pot[i - 1]
                arr_pot[i - 1] = arr_pot[i]
                arr_pot[i] = swap
                swap = arr[i - 1]
                arr[i - 1] = arr[i]
                arr[i] = swap
    return arr


def choicer(arr, k):
    beg_sum = sum(arr[i] for i in range(len(arr)))
    for i in range(len(arr)):
        arr[i] = (10 ** len(str(arr[i]))) - 1
        end_sum = sum(arr[i] for i in range(len(arr)))
        if i == k - 1: 
            return end_sum - beg_sum


numbs = min_sort(numbs, numbs_pot)
print(choicer(numbs, numb_of_choices))