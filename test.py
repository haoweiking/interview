# 1
a = 1
b = 2
a, b = b, a
print(a, b)
# 2
l1 = []
for i in range(3):
    l1.append({'num': i})
print(l1)
l2 = []
a = {'num': 0}
for i in range(3):
    a['num'] = i
    l2.append(a)
print(l2)
# 3 求两个集合的交集，并集和差集，说明结果的原因
set1 = {2,2.2, True, 4+3j}
set2 = {1, 2.2, False, 4+3j}
print(set1&set2) # True 和 1 可以相互间类型转换
print(set2&set1) # 保留 True 还是 1 取决于哪个在前面

print(set1|set2) # 优先保留 前面的集合中的元素
print(set2|set1)
