from collections import Counter
from icecream import ic
l1=[2,8,4,2,8,6,4,1,4,9,2,5,2,4,9] 
x = Counter(l1)
ic(x)
y=x.most_common(2)
ic(y)
second_e, count_second_e=y[1]
print(f"Second highest Element in List is{second_e},and its  count is {count_second_e}")










