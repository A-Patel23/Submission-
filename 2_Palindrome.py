# Determine whether a given string is Palindrome

def check_Palindrome(string):
    """     This function check the the given input sting is Palindrome string or not    """
    rinput_string = string.lower().replace(" ", "")  
    result = string == string[::-1]
    return result

print("Palindrome String")
string=input("Enter String : ")
print(check_Palindrome(string))