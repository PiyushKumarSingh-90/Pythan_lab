# d={}
# for i in range(1,11,2):
#     d[i]=i**3
    
# print(d)    

n = ""
topper = (0,)
while(n != "0" ):
    l = []
    n = input("\n\nEnter the name of topper (0 to exit)")
    if(n != "0"):
        for i in range(1,5):
            a = int(input(f"Enter marks for sub {i} : "))
            l.append(a)

        topper+=((n,l))
print(topper)        
        
max = 0
index = 0
for i in range(2,len(topper) , 2):
    sum = 0
    for j in topper[i]:
        sum += j

    if(sum>max):
        max = sum
        index = i
        
t = (topper[index-1] , topper[index])
print(t)
