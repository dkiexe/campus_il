# Write a function called sort_anagrams defined as follows:
# def sort_anagrams(list_of_strings):

# The function accepts as a parameter a list of strings, so each string is one word (without spaces).
# The function returns a list of the same strings that were transferred, but in the following way: 
# the list is divided into lists so that each "internal" list consists of words that are anagrams of each other 
# (anagram: a word consisting of letters of another word, i.e. the same letters but in a different order).

# Guidelines
# Make sure that the strings and lists are arranged according to the order in which the strings appear in the original list.

# Running examples of the sort_anagrams function
# >>> list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
# >>> sort_anagrams(list_of_words)
# [['deltas', 'desalt', 'slated', 'salted', 'staled', 'lasted'], ['retainers', 'ternaries'], ['pants'], ['generating', 'greatening '], ['smelters', 'termless', 'resmelts']]

# My solution
def sort_anagrams(list_of_strings):
    test_dict = {}
    for word in list_of_strings:
        sorted_word = str(sorted(word))
        if sorted_word in test_dict:
            test_dict[sorted_word].append(word)
        else:
            test_dict[sorted_word] = [word]
    return list(test_dict.values())[::-1]