# firstModule.py

def showAuthorInfo():
    name="Mehmet"
    surname="Gumustufek"
    studentNumber="211220025"
    authorNote="RTFUM"
    print(name,surname,studentNumber,authorNote)
def isLetter(char):
    return char.isalpha()

def toLowercase(letter):
    if letter.isupper():
        return letter.lower()
    return letter

def letterFrequency(text):
    text = text.replace(" ", "")
    letter_count = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    total_letters = sum(letter_count.values())
    frequency = {letter: (count / total_letters) * 100 for letter, count in letter_count.items()}
    return frequency

def countWords(text):
    words = text.split()
    return len(words)

def reverseString(s):
    return s[::-1]

def isPalindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]


# Test etmek için basit bir ana blok
if __name__ == "__main__":
    showAuthorInfo()
