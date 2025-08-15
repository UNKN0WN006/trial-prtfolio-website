# Bubble sort program to/for sorting numbers in ascending order
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example usage
numbers = [34, 7, 23, 32, 5, 62]
print("Original:", numbers)
print("Sorted:", bubble_sort(numbers))
