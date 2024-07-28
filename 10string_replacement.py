original_sentence = "I want to Python developer"
replacement_word = input("Type your favorite language! ")
result = original_sentence[ :10] + replacement_word+ original_sentence[-10:]
print(result)