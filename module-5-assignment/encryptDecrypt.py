def encrypt(S):
    encrypted = []
    i = 0
    while i < len(S):
        count = 1
        while i + 1 < len(S) and S[i] == S[i + 1]:
            count += 1
            i += 1
        encrypted.append(f"{count}{S[i]}")
        i += 1
    encrypted_string = ''.join(encrypted)[::-1]
    return encrypted_string

def decrypt(S):
    S = S[::-1]
    original = []
    i = 0
    while i < len(S):
        count = 0
        while i < len(S) and S[i].isdigit():
            count = count * 10 + int(S[i])
            i += 1
        original.append(S[i] * count)
        i += 1
    
    return ''.join(original)

S1 = "aaaaaaaaaaaa"
encrypted1 = encrypt(S1)
decrypted1 = decrypt(encrypted1)
print(f"Original: {S1}\nEncrypted: {encrypted1}\nDecrypted: {decrypted1}\n")

S2 = "ostad"
encrypted2 = encrypt(S2)
decrypted2 = decrypt(encrypted2)
print(f"Original: {S2}\nEncrypted: {encrypted2}\nDecrypted: {decrypted2}\n")
