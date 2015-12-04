def fibo(n):
    if n <= 1:
        return 1
    return fibo(n-1)+fibo(n-2)

def fibotail(n):
    def fibohelp(i,j,n):
        return fibohelp(j,i+j,n-1) if n>0 else j
    return fibohelp(0,1,n)

def fiboloop(n):
    firstfibo = 1
    secondfibo = 1
    nextfibo = 1
    
    for x in range(1,n-1):
        nextfibo = firstfibo + secondfibo
        firstfibo = secondfibo
        secondfibo = nextfibo

    return nextfibo
    
for x in range(1,300):
    f = fibotail(x)
    print("fibo(%d) = %d %s" % (x,f,type(f)))

    
        
