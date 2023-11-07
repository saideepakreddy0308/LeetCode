```
class Solution:
def backspaceCompare(self, s: str, t: str) -> bool:
# Stack Approach
temp = []
temp1 = []
if len(s) != 0 and len(t) != 0:
for i in s:
if '#'==i and len(temp) != 0:
temp.pop()
elif '#'==i and len(temp) == 0:
continue
else:
temp.append(i)
for i in t:
if '#'==i and len(temp1) != 0:
temp1.pop()
elif '#'== i and len(temp1) == 0:
continue
else:
temp1.append(i)
return (temp == temp1)
```