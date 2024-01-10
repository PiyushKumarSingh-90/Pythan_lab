n=int (input("\n\nEnter the no. of student : "))
l=[]
topper=()
for i in range(0,n):
   n= input("\nEnter the name of student : ")
   
   p=int(input("\nEnter the marks of physics : "))
   c=int(input("Enter the marks of chemistry : "))
   m=int(input("Enter the marks of maths : "))
   sum=p+c+m
   l.append(sum)
   print("_________________________________________")
   
   topper+=((n,sum)) 
print(topper) 

max=0
index=0

if(sum>max):
   max = sum
   index = i


t = (topper[index-1] , topper[index])
print("TOPPER IS :",t) 



