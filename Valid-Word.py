class Solution:
    def isValid(self, word: str) -> bool:
        isWord = True
        if len(word) < 3:
            print("Length less than 3")
            print(len(word))
            isWord = False
        n_vowels = 0
        n_alpha = 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for ch in word:
            if not(ch.isalpha() or ch.isdigit()):
                print("No alpha numeric")
                isWord = False
            if ch.isalpha():
                n_alpha += 1
            if ch in vowels:
                n_vowels += 1
        if not n_vowels:
            print("No vowels")
            isWord = False
        n_consonants = n_alpha - n_vowels
        if not n_consonants:
            print("No consonants")
            isWord = False

        return isWord

        