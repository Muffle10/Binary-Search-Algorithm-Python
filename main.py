arr = [1,10, 2, 1, 3, 4, 6, 4, 1, 4, 1, 2, 8, 9, 5, 6 ,9, 5, 5, 7, 5, 3]
inp = 10
found = ""
print("Array being searched:")
print(arr)
while len(arr) > 1:
    i = int(len(arr)/2)
    arr1 = arr[0:i]
    arr2 = arr[i:]
    if inp in arr1:
        arr = arr1
    elif inp in arr2:
        arr = arr2
    else:
        print("Num not found")
        found = False
        break
    print(arr)
if found:
    print(arr[0])
