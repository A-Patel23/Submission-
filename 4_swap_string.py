def swapString(first,second):
    '''  Swap two Strings Without Using any Third Variable   '''
    first,second=second,first
    print(f'Strings after swap\n First String = {first} \n Second String = {second}')

print("Before Swap")
a = input("Enter First String :")
b = input("Enter Second String :")

swapString(a,b)