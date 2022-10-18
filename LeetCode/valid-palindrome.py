class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_word = []

        for char in s:
            if char.isalnum():
                filtered_word.append(char.lower())

        string = ''.join(filtered_word)

        filtered_word.reverse()

        compare_string = ''.join(filtered_word)

        return string == compare_string
