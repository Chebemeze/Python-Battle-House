from collections import defaultdict

def group_anagrams_by_count(strs):
  anagrams = defaultdict(list)

  for word in strs:
    # Create a frequency array of size 26 for 'a'-'z'
    count = [0] * 26
    for char in word:
      count[ord(char) - ord("a")] += 1
    # Tuples are hashable and work as dictionary keys
    anagrams[tuple(count)].append(word)

  return list(anagrams.values())

print(group_anagrams_by_count(["eat", "tea", "ate", "listen", "silent", "act", "cat"]))
