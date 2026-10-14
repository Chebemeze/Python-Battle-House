from collections import defaultdict

def group_anagrams(words):
    #defaultdict() creates an empty list for new keys that doesn't exist.
    #so there is no possibility of running into KeyError,
    # because the value of the key becomes an empty list
    anagram = defaultdict(list)
    for word in words:
        #sort() sorts the characters and splits into a list of character
        #join() joins the characters back to a single word.
        b = "".join(sorted(word))
        anagram[b].append(word)
    return list(anagram.values())
print(group_anagrams(["eat", "tea", "ate", "listen", "silent", "act", "cat"]))
