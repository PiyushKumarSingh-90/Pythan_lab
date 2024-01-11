# wap that takes a list of strings as input and sorts them based on their length.


a = input("enter : ").split(" ")

print(a)

for i in range(0,len(a)):
    for j in range(i,len(a)):

        if(len(a[i]) > len(a[j])):
            temp = a[j]  
            a[j] = a[i]  
            a[i] = temp   

print(a)