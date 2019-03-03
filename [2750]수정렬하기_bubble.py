def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] >= arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            else:
                pass

N = int(input())
in_arr = []

for i in range(N):
    in_arr.append(int(input()))

bubble_sort(in_arr)

for i in in_arr:
    print(i)
