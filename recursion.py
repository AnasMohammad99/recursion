def fibonacci(x):
    #return the value of the index x of fibonacci
    assert x>=0 and int(x)==x,"n must be positive intger"
    if x in [1,0]:
        return x
    else:
        return fibonacci(x-1)+fibonacci(x-2)
#-----------------------------------------------------     
def sumOfDigits(x):
    assert x>=0 and int(x)==x,"n must be positive intger"
    if x==0:
        return x
    else:
        return (x%10 + sumOfDigits(int(x/10)))

#-----------------------------------------------------
def powerOfNum(x,n):
    #to calculate x**n 
    assert n>=0 and int(n)==n,"n must be positive intger"
    if n==0:
        return 1
    else:
        return x*powerOfNum(x,n-1)
#-----------------------------------------------------
def greatCommonDivisor(n1,n2):
    #find great positive integer common divisor for two numbers
    if n1%n2==0:
        assert n2>=0 and int(n2)==n2,"GCD must be positive intger"
        return n2
    else:
        return greatCommonDivisor(n2,n1%n2)
#-----------------------------------------------------
