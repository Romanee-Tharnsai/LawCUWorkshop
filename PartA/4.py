word1 = input("Input word:")
word2 = input("Input another word:")
if word1 == word1.upper() and word2 == word2.upper():
    print("Oops!")
elif word1 == word1.upper() or word2 == word2.upper():
    print(word1 + " " + word2)
else:
    print(word1 + word2)