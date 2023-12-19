def is_palindrome(sentence):
    cleaned_sentence = ''.join(char.lower() for char in sentence if char.isalnum())
    return cleaned_sentence == cleaned_sentence[::-1]



user_input = input()
result = is_palindrome(user_input)

if result :
    print("sentence is pldrne")
else:
    print("ssntnce")    



