 
def find_uniq(arr):
    # your code here
    arr.sort()

    if(arr[0] < arr[len(arr)-1] and arr[0] < arr[len(arr)-2]):
        n = arr[0]
    else:
        n = arr[len(arr)-1]


    return n   # n: unique integer in the array

# test.describe("Basic Tests")
print(find_uniq([ 1, 1, 1, 2, 1, 1 ])) # Return is number:, 2
print(find_uniq([ 0, 0, 0.55, 0, 0 ])) # Return is number:, 0.55
print(find_uniq([ 3, 10, 3, 3, 3 ])) # Return is number:, 10