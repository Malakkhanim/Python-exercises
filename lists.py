a=[1,2,12,4,100,100]
for i in range(3):
    a.insert(0,i)
a.sort()
print(a)
a.remove(max(a))
print(a)
