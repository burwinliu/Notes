class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0
        recordYes, recordNo = set(), set()
        for word in words:
            p = 0
            if word in recordYes:
                count += 1
                continue
            elif word in recordNo:
                continue
            for letter in s:
                if p == len(word):
                    break
                if letter == word[p]:
                    p += 1
            if p == len(word):
                count += 1
                recordYes.add(word)
            else:
                recordNo.add(word)
        return count