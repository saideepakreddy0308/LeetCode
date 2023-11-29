In a min-heap, the smallest element is at the root, and each node's value is less than or equal to the values of its children. While it may seem counterintuitive, we can use a min-heap to efficiently maintain the k largest elements.
​
Here's how it works:
​
Initialization:
Initially, we create a min-heap of size k with the first k elements of the array.
The root of this heap represents the smallest element among the k elements.
​
Iterating Through the Array:
As we iterate through the remaining elements in the array, we compare each element with the smallest element in the min-heap (the root).
If the current element is larger than the smallest element in the min-heap, we replace the smallest element with the current element.
This ensures that the min-heap always contains the k largest elements encountered so far.
​
Final Result:
After iterating through the entire array, the root of the min-heap will be the kth largest element.