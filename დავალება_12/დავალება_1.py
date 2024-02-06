

def num_of_words(value):
    split_value = value.split()
    word_count = {}

    for word in split_value:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
        
    return word_count


answer = input("Enter the text: ")
result = num_of_words(answer)       

print(result)