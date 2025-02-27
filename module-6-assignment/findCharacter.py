def find_kth_character(k):
    word = "a"

    while len(word) < k:
        new_word = "".join(chr((ord(c) - ord('a') + 1) % 26 + ord('a')) for c in word)
        word += new_word

    return word[k - 1]


print(find_kth_character(5))  
print(find_kth_character(10))