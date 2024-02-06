def char_in_string(input_string, target_char):
    count = 0
    for char in input_string:
        if target_char == char:
            count += 1
    return count


string = input("Enter a string: ").lower()
char = input("Enter a char: ").lower()


if len(char) == 1 and char.isalpha():
    result = char_in_string(string, char)
    print(f'The character count in string is {result}')
else:
    print("Please enter a valid single character.")



    