
def calculatio(x,y,z):
    result=0
    result=float(result)
    if z=='+':
        result=x+y
    elif z=='-':
        result=x-y
    elif z=='*':
        result=x*y
    if z=='/':
        if y==0:
            return "cannot divisible by zero"
        else:
            result=x/y
    return result
