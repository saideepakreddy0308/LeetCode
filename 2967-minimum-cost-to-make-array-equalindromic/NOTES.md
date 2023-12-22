Median minimizes Mean Absolute Error whereas mean minimizes Mean Squared Error
​
The sum of absolute deviations (=cost) from the median is always less than or equal to the sum of absolute deviations from the mean. The main reason is that the median is less sensitive to outliers than the mean.
​
Take the array: [1, 1, 1, 100]. The cost, if we use median, is 99. If we use mean it's a lot higher
​
**Working Process:**
1.  Sort the nums -> Go for middle element, its median
2.  if odd no.of elts, its median[midIndex] else if even no.of elts, it should be mid of middle elts (take average)
3.  Check if the num we get from through mid, if its palindrome, should be like [11,22,33,1,3] not like [21,23,34,32]
4. In any of the cases , if its not palindrome, check the left and right for next palindromic number, and total_cost minimized
5. if e,g [ 20,21,22] , we got mid as 21, so we choose 20,total_cost and 22,total_cost like p1 = mid - 1, p2 = mid +  1
6. Anyway 20 is not palandrome so it goes till 11, and right side it only goes tiil 20. And this point their return the min of both palindromic number's total costs.