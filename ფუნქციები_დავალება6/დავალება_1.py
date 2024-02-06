def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if sorted(str1) == sorted(str2):
        return f"{str1} and {str2} are anagrams"
    else:
        return f"{str1} and {str2} are not anagrams!"


print(are_anagrams("Listen", "silent"))
