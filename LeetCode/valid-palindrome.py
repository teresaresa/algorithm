import collections


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # list 를 쓰면 106ms, deque 를 쓰면 51ms
        filtered_word = collections.deque()

        for char in s:
            if char.isalnum():
                filtered_word.append(char.lower())

        string = ''.join(filtered_word)

        filtered_word.reverse()

        compare_string = ''.join(filtered_word)

        return string == compare_string
