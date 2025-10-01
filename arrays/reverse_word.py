class Solution:
    def reverseWords(self, s: str) -> str:
        lst_words = []

        i = 0
        while i < len(s):
            curr_word = ""
            if s[i] != " ":
                j = i
                while j < len(s) and s[j] != " ":
                    curr_word += s[j]
                    j += 1
                lst_words.append(curr_word)
            if curr_word:
                i += len(curr_word)
            else:
                i += 1
        lst_words.reverse()
        return " ".join(lst_words)

sol = Solution()
print(sol.reverseWords("the sky is blue"))
print(sol.reverseWords("   hello   world  "))