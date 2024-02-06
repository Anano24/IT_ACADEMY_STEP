import string

answer = input("შეიყვანეთ ტექსტი: ").lower()

# Remove spaces and punctuation from the input text.
translator = str.maketrans("", "", string.punctuation + " ")
text_without_punctuation = answer.translate(translator)


if text_without_punctuation == text_without_punctuation[::-1]:
    print("ტექსტი არის პალინდრომი")
else:
    print("ტექსტი არ არის პალინდრომი!")
