def is_k_ostad(str1, str2, k):
    if len(str1) == len(str2):
        diff_count = sum(1 for i in range(len(str1)) if str1[i] != str2[i])
    else:
        diff_count = abs(len(str1) - len(str2))

    if diff_count <= k:
        return "Yes"
    else:
        return "No"



str1 = "anagram"
str2 = "grammar"
k = 3
print(is_k_ostad(str1, str2, k)) 

str1 = "ostad"
str2 = "boss"
k = 1
print(is_k_ostad(str1, str2, k)) 
