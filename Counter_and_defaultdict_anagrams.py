"""This function uses Counter to automatically count words. it forms a dictionary of each character and it's count
    default creates a dictionary where each key not already in the dictionary is given an empty list. defaultdict
    continues to do this dynamically upon every key search.
"""

from collections import Counter, defaultdict
def count_and_defaultdict_anagrams(words):
    anams = defaultdict(list)
    for word in words:
        counts = Counter(word) #returns a dictionary of counting the words

        key = tuple(sorted(counts.items()))
        anams[key].append(word)
    return list(anams.values())
print(count_and_defaultdict_anagrams(["eat", "tea", "ate", "listen", "silent", "act", "cat"]))
