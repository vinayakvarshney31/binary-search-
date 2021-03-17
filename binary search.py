a=['charger','earphone','laptop','mobile','shoes','watch','pen','pencil','paper']
for i in range(len(a)):
    for j in range(len(a)):
        if a[i] < a[j]:
            a[i],a[j]=a[j],a[i]
        else:
            continue
print(a)
b=input("enter the element to be searched")
b=b.lower()
r=0
l=len(a)
for i in range(len(a)):
       middle=(r+l)/2
       middle=int(middle)
       if a[middle] == b:
         print("element found at index",middle)
         break
       elif b < a[middle]:
         l=middle-1
       else:
         r=middle+1
if r>l:
    print("element not found")
