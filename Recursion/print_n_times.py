# Print Name N times

def counting(n,i=0):
    if(i<n):
        print("Sujal")
        counting(n,i+1)

counting(5)

#print  linear series till N


def counting(n,i=0):
    if(i<n):
        print(i+1)
        counting(n,i+1)
counting(10)

#Linear reverse order n to 1

def counting(n):
    if n>0:
        print(n)
        counting(n-1)

counting(10)