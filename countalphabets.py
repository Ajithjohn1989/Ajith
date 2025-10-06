s="java"
counter={}
for v in s:
    if v in counter:
        counter[v]=counter[v]+1
    else:
        counter[v]=1
print(counter)