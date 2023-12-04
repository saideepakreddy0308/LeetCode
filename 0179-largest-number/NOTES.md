Idea / Approach: To solve this problem is to find a custom sorting order for the numbers, that result in the formation of the largest possible number
​
This solution uses the cmp_to_key function from the functools module to convert the custom comparator function to a key function, which is required for the sorted function in Python. The key function is used to determine the sorting order.
_____________________________
3 Method:
​
The LargerNumKey class is a subclass of the built-in str class that overrides the less than operator (<) to compare two strings in a special way. The lt method is called when we use the less than operator to compare two strings. We define the method to compare two strings x and y in the following way:
​
Concatenate x and y in reverse order: x+y.
Concatenate y and x in reverse order: y+x.
Compare the two concatenated strings in reverse order to get descending order. That is, if x+y is greater than y+x, we return True. Otherwise, we return False.
​
In the largestNumber method, we first convert the list of numbers to a list of strings. We then sort the list of strings using our custom sorting function. Finally, we join the sorted list of strings to form the largest number.
​
Note that if the largest number is 0, we return "0" instead of the actual largest number. This is because "0" is the only case where the leading digit is "0".
​