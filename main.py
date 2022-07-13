arr = [1,10, 2, 1, 3, 4, 6, 4, 1, 4, 1, 2, 8, 9, 5, 6 ,9, 5, 5, 7, 5, 3]
# A random array I made
inp = 10
# input - the number we need to find
found = ""
# Declaring variable called found globally
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
# Sorting Algorithm


if found:
    print(arr[0])
 # Prints out found number in array;
