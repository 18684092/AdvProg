##############
# Problem 59 #
##############

# XOR Decryption

"""
Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.
"""

import time
def loadWords():
    with open('words_alpha.txt') as File:
        words = set(File.read().split())
    return words

def loadCipherText():
    with open('p059_cipher.txt', 'r') as f:
        results = []
        for line in f:
            words = line.split(',')
            results.append(words)
    cipherString = ""
    for line in results:
        for a in line:
            cipherString += chr(int(a))
    return(cipherString) 

if __name__ == '__main__':
    start = time.time()
    englishWords = loadWords()
    cipherText = loadCipherText()
    print("###################")
    print("# Convert this... #")
    print("###################")
    for c in cipherText:
        if ord(c) < 32:
            print(".",end="")
        else:
            print(c,end="")
    print()
    for first in range(97, 123):
        for second in range(97, 123):
            for third in range(97, 123):
                lengthMinus = len(cipherText) % 3
                string = cipherText
                for i in range(0,len(cipherText) - lengthMinus, 3):
                    threeChars = chr(ord(string[i]) ^ first) + chr(ord(string[i + 1]) ^ second) + chr(ord(string[i + 2]) ^ third)
                    string = string[:i] + threeChars + string[i + 3:]
                if lengthMinus == 1:
                    string = string[:-1] + chr(ord(string[-1]) ^ first)
                elif lengthMinus == 2:
                    string = string[:-2] + chr(ord(string[-2]) ^ first) + chr(ord(string[-1]) ^ second)
                spaces = []
                for i, c in enumerate(string):
                    if c == " ":
                        spaces.append(i)
                if len(spaces) > 50:
                    words = []
                    for i in range(1,len(spaces) - 2):
                        words.append(string[spaces[i]:spaces[i+1]].strip())
                    valid = 0
                    for word in words:
                        if word in englishWords:
                            valid += 1
                    if valid > 0.5 * len(spaces):
                        print("##############")
                        print("# To this... #")
                        print("##############")        
                        print(string + "\n")
                        finalSum = 0
                        for i in string:
                            finalSum += ord(i)
                        print("Sum of all ascii characters:", finalSum)
                        end = time.time()
                        print("Time Taken:", int((end - start) * 100) / 100, "Seconds")
                        quit()
