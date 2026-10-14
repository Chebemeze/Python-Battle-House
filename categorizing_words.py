def categorizing_words(words):
    b = {}
    for i in words:
        len_x = len(i)
        if len_x not in b:
            b[len_x]= [i]
        else:
            b[len_x].append(i)
    return b
print(categorizing_words(["Eben", "Golden", "Benji", "dokwe"]))
