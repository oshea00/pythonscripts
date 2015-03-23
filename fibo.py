def fibo(n):
    if n <= 1:
        return 1
    return fibo(n-1)+fibo(n-2)

def fibotail(n):
    def fibohelp(i,j,n):
        return fibohelp(j,i+j,n-1) if n>0 else j
    return fibohelp(0,1,n)

for x in range(1,300):
    f = fibotail(x)
    print("fibo(%d) = %d %s" % (x,f,type(f)))

    
        
