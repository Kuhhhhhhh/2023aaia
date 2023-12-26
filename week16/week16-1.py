# "00111" 想知道左邊幾個0、右邊幾個1 加起來多
class Solution:
    def maxScore(self, s: str) -> int:
        N = len(s) #字串長度
        ans = 0 #迴圈前面，答案是0
        for left in range(N-1):
            #接下來測測看左邊幾個0、右邊幾個1
            now = 0 #現在測試的值是多少
            for i in range(N): #每個字母都檢查
                if i<=left and s[i]=='0':now += 1 #左邊的0
                if i>left and s[i]=='1': now += 1 #右邊的1
            if now>ans: ans = now #迴圈中間，更新答案
        return ans #迴圈後面，答案算出來
