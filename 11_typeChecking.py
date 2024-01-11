def fact(n):
    if n==0:
        return 1
    elif n<0:
        return("invalid input,Enter integer value")

    else:
        recurse=n*fact(n-1)
        return recurse

n=-1.2

while(not(int(n)==n)):    
    try:   
        n=int(input("Enter the no. : ")) 
    except:
        print("ERROR AAYA") 

print(fact(n))
