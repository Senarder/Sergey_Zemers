def first_not_repeat_letter(word):
    for i in range(len(word)):
        count = 0
        for j in range(i+1, len(word)):
            if word[i] == word[j]:
                count += 1
        if count == 0:
            return word[i]
    return None


print(first_not_repeat_letter("ffgkTfgtkl"))
print(first_not_repeat_letter("ababababa"))
print(first_not_repeat_letter("aboba"))