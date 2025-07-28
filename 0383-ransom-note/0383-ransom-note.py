from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = Counter(ransomNote) # a 2개 b 1개
        magazine_count = Counter(magazine) # a 2개 b 1개 c 5개

        for char, count in ransom_count.items():
            if magazine_count[char] < count: #  a 2개 b 1개 똑같아.
                return False
        
        return True