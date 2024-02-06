def revers_str(string):
   
    if len(string) <= 1:
        return string
    else:
        return revers_str(string[1:]) + string[0]

input_str = input("Enter string: ").lower()
print(revers_str(input_str))