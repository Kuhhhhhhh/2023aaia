#每日挑戰題23/12/01:1662. Check If Two String Arrays are Equivalent
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        a = ''.join(word1) #課本第二章有教split() 和 .jion()
        b = ''.join(word2) # 單單.join(word2)

        if a==b: return True 
        else: return False
        