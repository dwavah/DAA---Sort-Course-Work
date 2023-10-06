# DAA---Sort-Course-Work
Research on Quick Sort, Counting Sort and Heap Sort 


WAVAMUNNO DANIEL L - S23B23/091
DAA

1. QUICK SORT
Quick sort is a sorting algorithm based on the divide and conquer algorithm that picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array.
Quick sort is a highly efficient sorting algorithm and is based on partitioning of array of data into smaller arrays.

Explanation
Quicksort using list comprehension is a recursive algorithm for sorting an array of elements. It works by selecting a pivot element and partitioning the array around the pivot, such that all elements less than the pivot are moved to its left and all elements greater than the pivot are moved to its right. Then, it recursively applies the same process to the left and right sub-arrays until the entire array is sorted.
Algorithm:
If the input array has length 0 or 1, return the array as it is already sorted.
Choose the first element of the array as the pivot element.
Create two empty lists, left and right.
For each element in the array except for the pivot:
a. If the element is smaller than the pivot, add it to the left list.
b. If the element is greater than or equal to the pivot, add it to the right list.
Recursively call quicksort on the left and right lists.
Concatenate the sorted left list, the pivot element, and the sorted right list.
Return the concatenated list.

Analysis
Worst Case Complexity [Big-O] is O(n2). It occurs when the pivot element picked is either the greatest or the smallest element.
Best Case Complexity [Big-omega] is O(n*log n). It occurs when the pivot element is always the middle element or near to the middle element.
Average Case Complexity [Big-theta] is O(n*log n). It occurs when the above conditions do not occur.




2. COUNTING SORT
Counting sort is a non-comparison-based sorting algorithm that works well when there is limited range of input values. It is particularly efficient when the range of input values is small compared to the number of elements to be sorted. The basic idea behind counting sort is to count the frequency of each distinct element in the input array and use that information to place the elements in their correct sorted positions.

Explanation
Counting Sort is a sorting algorithm that works by counting the occurrence of each distinct element in the input list and using that information to determine the position of each element in the output list. The algorithm has a time complexity of O(n+k), where n is the number of elements in the input list and k is the range of the input data, and a space complexity of O(k).
Algorithm:
Convert the input string into a list of characters.
Count the occurrence of each character in the list using the collections.Counter() method.
Sort the keys of the resulting Counter object to get the unique characters in the list in sorted order.
For each character in the sorted list of keys, create a list of repeated characters using the corresponding count from the Counter object.
Concatenate the lists of repeated characters to form the sorted output list.

Analysis
Worst Case Complexity is O(n+k)
Best Case Complexity is O(n+k)
Average Case Complexity is O(n+k)
In all the above cases, the complexity is the same because no matter how the elements are placed in the array, the algorithm goes through n+k times.




3. HEAP SORT
Heap sort is a comparison-based sorting technique based on Binary Heap data structure. It is similar to the selection sort where we first find the minimum element and place the minimum element at the beginning. Repeat the same process for the remaining elements.
Heap Sort can also work by building a binary heap and repeatedly extracting the maximum element from the heap, which is then placed at the end of the sorted portion of the array.
 
Explanation
Import the Python STL library “heapq“.
Convert the input list into a heap using the “heapify” function from heapq.
Create an empty list “result” to store the sorted elements.
Iterate over the heap and extract the minimum element using “heappop” function from heapq and append it to the “result” list.
Return the “result” list as the sorted output.

Analysis
Heap Sort has O(n log n) time complexities for all the cases ( best case, average case, and worst case).


