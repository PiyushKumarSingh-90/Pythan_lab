# wap that converts camel case string to snake case.

a = input("Enter  : ")
str=""

index=0
for i in a:
    
    if  i.isupper():
        str=a[:index]+"_"+a[index:].lower()
    index+=1 

print(str)




