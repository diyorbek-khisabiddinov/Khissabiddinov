k = int(input())
n = int(input())
cnt = 0
list = []
dict = {}
my_set = set()
for i in range(k,n,1):
    if i%3==0 or i%5==0:
        cnt+=1
        list.append(i)
        my_set.add(i)
for i in range(cnt):
    dict[i]=list[i]
print(list)
print(my_set)
print(dict)


