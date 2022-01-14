n=int(input("enter the number of values in a list:"))
print("enter the numbers present in the list:")
a=[]
for i in range(0,n):
  x=int(input(f"enter {i+1}th value:"))
  a.append(x)

for i in range(0,n-1):
  for j in range(i+1,n):
    if a[i]>a[j]:
      a[i],a[j]=a[j],a[i]
print("---------------")
print("sorted List is:")
print("---------------")
for i in range(0,n):
  print(a[i])
