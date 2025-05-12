class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = re.sub(r'[^a-z0-9]', '', s.lower())
        for i in range(len(cleaned_string) // 2) :
            if cleaned_string[i] != cleaned_string[-1 - i]:
                return False
        return True
        