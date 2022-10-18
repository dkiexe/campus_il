# Write a function called translate defined as follows:
# def translate(sentence):
#      words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the' }
# The function accepts as a parameter a string that represents a sentence in the Spanish language and returns a new string that is a translation of the sentence in the English language.

# For the sake of simplicity, 
# translate each word in the sentence using the words dictionary that appears inside the translate function. 
# Check that your code works using it (you can also expand the dictionary if you want).

# An example of running the translate function:
# print(translate("el gato esta en la casa"))
# the cat is in the house
# Guidelines:

# Realize the function to use a generator expression.

# My solution
def translate(sentence):
    sentence_break= sentence.split(' ')
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    final_sentance_translated= (words[x] for x in sentence_break if x in words.keys())
    return " ".join(final_sentance_translated)

print(translate("el gato esta en la casa"))