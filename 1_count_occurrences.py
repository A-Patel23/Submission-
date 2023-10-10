def count_occurrences(inp_String,character):
    '''        This function return occurrences of a given character in any inputed string.    '''
    counter=0
    for i in inp_String:
        if i == character:
            counter+=1
    result =f"Input string {inp_String} have {counter} time {character}."
    return result

print("Occurance of character in a string.")
inp_String=input("Enter String : ")
character=input("Enter Character : ")
print("Output :", count_occurrences(inp_String,character))