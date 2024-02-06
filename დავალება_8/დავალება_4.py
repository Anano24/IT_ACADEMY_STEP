
lst = ['kaiak', 'apple', 'radar', 'hello', 'madam']

palindrome = list(filter(lambda x: x == x[::-1], lst))

print(f'Palindromes are this strings: {palindrome}')