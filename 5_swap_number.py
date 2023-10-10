def swapString(a,b):
    '''  Swap two number using arithmetic operations    '''
    
    a = a + b 
    b = a - b 
    a = a - b 
    print("X : ",a,"\nY : ",b)

print("Before Swap")
a = int(input("Enter First Number :"))
b = int(input("Enter Second Number :"))

swapString(a,b)