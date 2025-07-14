def with_return(a,b):
    result = a+b 
    return result

ans = with_return(3,5)
print(ans)

def without_return(a,b):
    result = a+b
    print(result)

without_return(32,33)